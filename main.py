import pandas as pd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt

path = "/Users/rtimganov/Downloads/Filter for TK board (Taker).csv"
start_dt = "Created"
end_dt = "Resolved"
columns = ["Issue key", "Summary", start_dt, end_dt]
df = pd.read_csv(path, usecols=columns,
                 parse_dates=[start_dt, end_dt])
df["To Test"] = (df[end_dt] - df[start_dt]).dt.days
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print((df[["Summary", "To Test"]]))
print("85%% test = ", df["To Test"].quantile(0.85))

