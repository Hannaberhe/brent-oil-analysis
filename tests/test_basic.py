"""Basic tests."""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    import pandas
    import numpy
    assert True

def test_utils():
    from src.data_utils import compute_log_returns
    import pandas as pd
    df = pd.DataFrame({'Price': [10, 11, 12]})
    returns = compute_log_returns(df)
    assert len(returns) == 3
    assert returns.iloc[0] != returns.iloc[0]  # NaN check
