import pandas as pd
import numpy as np

def fill_missing_linear(ts):
    # Fill missing values using linear interpolation
    return ts.interpolate(method = "linear")

# Sample time series with missing values
dates = pd.date_range("2022-06-01", periods=6, freq="D")
data = [2.0, np.nan, np.nan, 8.0, np.nan, 12.0]
ts = pd.Series(data, index=dates)

filled_ts = fill_missing_linear(ts)
print(filled_ts)