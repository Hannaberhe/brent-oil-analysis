import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load oil data
df = pd.read_csv('data/BrentOilPrices.csv', parse_dates=['Date'])
print(f"Data: {len(df)} rows")
print(f"Range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Price: min=${df['Price'].min():.2f}, max=${df['Price'].max():.2f}, mean=${df['Price'].mean():.2f}")

# Load events
events = pd.read_csv('data/events.csv')
events['date'] = pd.to_datetime(events['date'])
print(f"\nEvents: {len(events)} documented")

# Plot price with events
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df['Date'], df['Price'], color='blue', linewidth=1)
ax.set_title('Brent Oil Price (1987-2022) with Major Events')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD/barrel)')

for _, event in events.iterrows():
    ax.axvline(event['date'], color='red', alpha=0.3, linewidth=1)
    ax.text(event['date'], df['Price'].max()*0.95, event['event'], 
            rotation=90, fontsize=7, verticalalignment='top')

plt.tight_layout()
plt.savefig('reports/oil_price_events.png', dpi=150)
print("Chart saved")

# Log returns
df['log_return'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
print(f"\nLog returns: mean={df['log_return'].mean():.6f}, std={df['log_return'].std():.4f}")

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(df['Date'], df['log_return'], color='green', alpha=0.7, linewidth=0.5)
ax.set_title('Brent Oil Log Returns')
ax.set_xlabel('Date')
plt.tight_layout()
plt.savefig('reports/log_returns.png', dpi=150)
print("Log returns chart saved")
print("\nDone")
