

import pandas as pd
import numpy as np

data = pd.read_csv("bank-full.csv", sep=';')
print(data.head())
print("Null values:\n", data.isnull().sum())
print("\nUnknown values:\n", (data == "unknown").sum())


data = data.replace("unknown", np.nan)

cat_cols = data.select_dtypes(include='object').columns

for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])


num_cols = data.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    data[col] = data[col].fillna(data[col].median())

print(data.isnull().sum())

data['pdays_contacted'] = data['pdays'].apply(lambda x: 0 if x == -1 else 1)
print(data.head())
data = pd.get_dummies(data, drop_first=True)
print("Encoded")
print(data.head())
print(data.columns)
print(data['job_student'].head(5))
print(data['job_management'].head(5))
print(data['job_entrepreneur'].head(5))
print(data['job_services'].head(5))
