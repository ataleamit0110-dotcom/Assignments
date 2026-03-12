import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = pd.read_csv("Advertising.csv")
print(data.head())
print(data.head())
data.drop(columns=["Unnamed: 0"], inplace=True)
print(data.head())


x = data[["TV", "radio", "newspaper"]]
y = data["sales"]

print("X values ", x)
print("Y values ", y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

print("X train ", x_train)
print(" x_test ", x_test)
print(" y_train ", y_train)
print(" y_test ", y_test)


model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("y+pred ", y_pred)
print("actual y  ", y_test.values)


#Accuracy= Total Predictions/Correct Predictions (/ means divided by )
#accuracy = accuracy_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
