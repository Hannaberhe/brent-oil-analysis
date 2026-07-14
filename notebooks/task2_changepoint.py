import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/BrentOilPrices.csv', parse_dates=['Date'])
prices = df['Price'].values
print(f"Data: {len(prices)} days")

# Change point detection using PELT
model = rpt.Pelt(model="rbf").fit(prices)
change_points = model.predict(pen=10)
print(f"Found {len(change_points)-1} change points")

# Get dates of changes
change_dates = [df['Date'].iloc[cp-1] for cp in change_points[:-1]]
print("Change dates:")
for d in change_dates:
    print(f"  {d.date()}")

# Price with change points
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], prices, color='blue', alpha=0.7, linewidth=0.8)
for cp in change_points[:-1]:
    ax.axvline(df['Date'].iloc[cp-1], color='red', linestyle='--', alpha=0.5)
ax.set_title('Brent Oil Price with Detected Change Points')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
plt.tight_layout()
plt.savefig('reports/price_with_changepoint.png', dpi=150)
print("Chart saved")

# Compare with events
events = pd.read_csv('data/events.csv')
events['date'] = pd.to_datetime(events['date'])
print("\nEvent matching:")
for d in change_dates:
    close_events = events[(events['date'] - d).dt.days.abs() < 90]
    if len(close_events) > 0:
        print(f"  {d.date()} - near: {close_events['event'].values[0]}")

print("\nDone")
