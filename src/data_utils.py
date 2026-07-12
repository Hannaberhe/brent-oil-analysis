"""Data utilities with error handling."""
import pandas as pd
import numpy as np
import os

def load_oil_data(filepath='data/BrentOilPrices.csv'):
    """Load Brent oil price data safely."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        df = pd.read_csv(filepath, parse_dates=['Date'])
        if 'Price' not in df.columns:
            raise ValueError("Missing 'Price' column")
        print(f"Loaded {len(df)} rows")
        return df
    except Exception as e:
        raise ValueError(f"Error reading {filepath}: {e}")

def load_events(filepath='data/events.csv'):
    """Load events data safely."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        events = pd.read_csv(filepath)
        events['date'] = pd.to_datetime(events['date'])
        return events
    except Exception as e:
        raise ValueError(f"Error reading {filepath}: {e}")

def compute_log_returns(df, price_col='Price'):
    """Compute log returns from price column."""
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found")
    return np.log(df[price_col]) - np.log(df[price_col].shift(1))
