

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

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



X = data.drop("y_yes", axis=1)
y = data["y_yes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


scaler = StandardScaler()

# Fit only on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)



# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_scaled, y_train)

# KNN
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)


y_pred_log = log_model.predict(X_test_scaled)
y_pred_knn = knn_model.predict(X_test_scaled)
y_pred_rf = rf_model.predict(X_test)


