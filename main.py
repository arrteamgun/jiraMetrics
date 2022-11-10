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

columns = ["Issue key", "Issue Type", "Custom field (ToDo datetime)", "Custom field (InTesting datetime)"]

df = pd.read_csv("/Users/rtimganov/Downloads/FH Data/LIS3(10-14S).csv", usecols=columns,
                 parse_dates=["Custom field (ToDo datetime)", "Custom field (InTesting datetime)"])
df["To Test"] = (df["Custom field (InTesting datetime)"] - df["Custom field (ToDo datetime)"]).dt.days
df_test_85 = df["To Test"].quantile(0.85)
#print(df.to_string())
#print("85% percentile:", df_test_85)

df_test = df[df["Issue Type"] != "Epic"]
df_test_true = df_test[df_test["Issue Type"] != "Story"]
print(df_test_true)
print("85%% = ", df_test_true["To Test"].quantile(0.85))