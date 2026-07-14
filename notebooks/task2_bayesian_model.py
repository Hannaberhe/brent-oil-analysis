import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymc as pm
import arviz as az
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/BrentOilPrices.csv', parse_dates=['Date'])
prices = df['Price'].values
days = np.arange(len(prices))
print(f"Data: {len(prices)} days")

prices_sub = prices[::5]
days_sub = days[::5]
print(f"Subset: {len(prices_sub)} points")

print("Building model...")
with pm.Model() as model:
    tau = pm.DiscreteUniform('tau', lower=0, upper=len(prices_sub)-1)
    mu1 = pm.Normal('mu1', mu=np.mean(prices_sub), sigma=50)
    mu2 = pm.Normal('mu2', mu=np.mean(prices_sub), sigma=50)
    sigma = pm.HalfNormal('sigma', sigma=20)
    mu = pm.math.switch(tau >= days_sub, mu1, mu2)
    likelihood = pm.Normal('likelihood', mu=mu, sigma=sigma, observed=prices_sub)

print("Sampling...")
with model:
    trace = pm.sample(1000, tune=500, chains=2, random_seed=42, progressbar=False)

summary = az.summary(trace)
print(summary)

tau_samples = trace.posterior['tau'].values.flatten()
change_day = int(np.median(tau_samples)) * 5
change_date = df['Date'].iloc[change_day]
print(f"\nChange point: {change_date.date()}")

mu1_mean = trace.posterior['mu1'].values.flatten().mean()
mu2_mean = trace.posterior['mu2'].values.flatten().mean()
print(f"Before: ${mu1_mean:.2f}, After: ${mu2_mean:.2f}")

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], prices, color='blue', alpha=0.7, linewidth=0.8)
ax.axvline(change_date, color='red', linestyle='--', linewidth=2, label=f'Change: {change_date.date()}')
ax.set_title('Brent Oil Price with Detected Change Point')
ax.legend()
plt.tight_layout()
plt.savefig('reports/price_with_changepoint.png', dpi=150)
print("Chart saved")
print("Done")
