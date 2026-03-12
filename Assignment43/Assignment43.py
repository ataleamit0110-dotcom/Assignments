import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Load data
data = pd.read_csv("PlayPredictor.csv")
print(data.head())
data.drop(columns=["Unnamed: 0"], inplace=True)
print(data.head())


lblEncoder = LabelEncoder()
lblEncoder.fit(data["Whether"])
data["Whether"] = lblEncoder.transform(data["Whether"])

lblEncoder.fit(data["Temperature"])
data["Temperature"] = lblEncoder.transform(data["Temperature"])

lblEncoder.fit(data["Play"])
data["Play"] = lblEncoder.transform(data["Play"])
print(data)

x = data[["Whether", "Temperature"]]
y = data["Play"]

print("Print x")
print(x)
print("Print y ")

print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.1, random_state=42)

print("X train ", x_train)
print(" x_test ", x_test)
print(" y_train ", y_train)
print(" y_test ", y_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

y_prediction = model.predict(x_test)
print("y+pred ", y_prediction)
print("actual y  ", y_test.values)


#Accuracy= Total Predictions/Correct Predictions (/ means divided by )
accuracy = accuracy_score(y_test, y_prediction)

print("accuracy ", accuracy)


new_data = pd.DataFrame([[2,1]], columns=["Whether","Temperature"])# # Sunny + Hot
prediction = model.predict(new_data)

print(prediction)







