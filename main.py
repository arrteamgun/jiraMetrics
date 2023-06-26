import pandas as pd
import datetime as dt
import numpy as np

path = "/Users/rtimganov/Downloads/Taker Stat/ig stories.csv"
start_dt = "Created"
end_dt = "Resolved"
columns = ["Issue key", "Summary", "Issue Type", start_dt, end_dt]
df = pd.read_csv(path, usecols=columns, parse_dates=[start_dt, end_dt])
df["To Test"] = (df[end_dt] - df[start_dt]).dt.days
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print((df[["Summary", "To Test"]]))
    df.to_csv("/Users/rtimganov/Downloads/Taker Stat/ig_stories_table.csv")
print("85%% test = ", df["To Test"].quantile(0.85))