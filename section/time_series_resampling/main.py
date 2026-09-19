import pandas as pd

def resample_to_weekly_sum(values):
    weekly_sum = values.resample('W').sum()
    return weekly_sum

# Sample daily time series
dates = pd.date_range("2024-01-01", periods=14, freq="D")
values = pd.Series(range(1, 15), index=dates)

result = resample_to_weekly_sum(values)
print(result)