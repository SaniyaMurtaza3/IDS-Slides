import pandas as pd
import numpy as np
import statistics as st
import os
os.chdir(r'E:\BS Teaching\Fall2022\IDS\PyProgs\CSV_Files')
data = pd.read_csv("DataFile.csv")
# print(data.head())
# print(type(data))
# print(data.size) # shape, size
# rows = len(data.axes[0])
# print("number of rows: " + str(rows))
# cols = len(data.axes[1])
# print("number of cols: " + str(cols))

# print(data.columns)
# print(data.describe(include='all')) # include = number, all, or object
sdata = data['Salary'] # data.Salary
# sdata = data.iloc[0:3,2:4] # [rows,cols], [r_s:r_e,c_s:c_e]
# print(sdata)
# meanval = st.quantiles(sdata) # median, mode, quantiles
# print(meanval)
# qv = st.stdev(data.Salary)
# print(qv)

# Write to File
# header = ['Name', 'Gender', 'New Age', 'New Salary']
col1 = data.Name
col2 = data.Gender
col3 = data.Age + 5
col4 = data.Salary * 1.50
frame = {'Name':col1, 'Gender':col2, 'New Age':col3, 'New Salary':col4}
df = pd.DataFrame(frame)
# # # #
df.to_csv('New Data.csv')
print(df)