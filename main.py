import pandas as pd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
'''columns = ["Issue key", "Custom field (Analysis datetime)",
           "Custom field (Approve datetime)", "Custom field (InProgress datetime)",
           "Custom field (InTesting datetime)",
           "Custom field (Planning datetime)", "Custom field (Prod datetime)",
           "Custom field (ReadyForPlanning datetime)", "Custom field (ReadyForQA datetime)",
           "Custom field (ReadyForRelease datetime)", "Custom field (Release datetime)",
           "Custom field (ToDo datetime)"]'''

#columns = ["Issue key", "Issue Type", "Custom field (ToDo datetime)", "Custom field (InTesting datetime)", "Custom field (Story Points)"]


lis3 = "/Users/rtimganov/Downloads/FH Data/LIS3(10-14S).csv"
wm4 = "/Users/rtimganov/Downloads/FH Data/Web Mobile 4.csv"
wm_stories = "/Users/rtimganov/Downloads/FH Data/web stories 3m.csv"

start_dt = "Custom field (Start date)"
end_dt = "Custom field (End date)"
ready_dt = "Custom field (Ready date)"
release_dt = "Custom field (Release datetime)"

columns = ["Issue key", "Summary", start_dt, end_dt, ready_dt, release_dt]

df = pd.read_csv(wm_stories, usecols=columns,
                 parse_dates=[start_dt, end_dt, ready_dt, release_dt])

df["To Test"] = (df[end_dt] - df[start_dt]).dt.days
df["To Release"] = (df[ready_dt] - df[end_dt]).dt.days
df["To Prod"] = (df[release_dt] - df[ready_dt]).dt.days
df["Total"] = (df[release_dt] - df[start_dt]).dt.days
#print(df.to_string())
#print("85% percentile:", df_test_85)
#df_test = df[df["Issue Type"] == "Story"]
#df_test_true = df_test[df_test["Issue Type"] != "Story"]

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print((df[["Summary", "To Test", "To Release", "To Prod", "Total"]].to_markdown()))

print("85%% test = ", df["To Test"].quantile(0.85))
print("85%% release = ", df["To Release"].quantile(0.85))
print("85%% prod = ", df["To Prod"].quantile(0.85))
print("85%% total =", df["Total"].quantile(0.85))
#to do - prod
#to do - check filters