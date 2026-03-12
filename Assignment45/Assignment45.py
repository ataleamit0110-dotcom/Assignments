import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("WinePredictor.csv")
print(data)

X = data.drop("Class", axis = 1)
Y = data["Class"]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)


print("After scaled X_train", X_train)
print("After scaled X_test", X_test)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)

for i in range(len(y_pred)):
    print("Actual:", Y_test.values[i], "Predicted:", y_pred[i])

accuracy = accuracy_score(Y_test, y_pred)
print("Accuracy :", accuracy)






