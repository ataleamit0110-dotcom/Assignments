# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix
# # step 1 load dataset

# dataSetPath = "student_performance_ml1.csv"
# df = pd.read_csv(dataSetPath)
# print("First 5 rows",df.head())
# print("last 5 rows\n",df.tail())
# print("Shape of dataset - Total number of rows and columns\n",df.shape)
# print("Columns in dataset\n",df.columns)
# print("Data types of each column\n",df.dtypes)


# feature_cols = [
#     "StudyHours",
#     "Attendance",
#     "PreviousScore",
#     "AssignmentsCompleted",
#     "SleepHours"
# ]
# X = df[feature_cols]
# Y = df["FinalResult"]
# print("X shape ", X.shape)
# print("Y Shape ", Y.shape)


# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# model = DecisionTreeClassifier(max_depth=2)
# model.fit(X_train, Y_train)

# yPredicted = model.predict(X_test)
# accuracy = accuracy_score(Y_test, yPredicted)
# print("accuracy ", accuracy)

# conf_metrix = confusion_matrix(Y_test, yPredicted)
# print("Confusion metrix", conf_metrix)

# print("Train Accuracy:", model.score(X_train, Y_train))
# print("Test Accuracy:", model.score(X_test, Y_test))



# from sklearn.model_selection import cross_val_score

# scores = cross_val_score(model, X, Y, cv=5)
# print("Cross Validation Accuracy:", scores)
# print("Mean Accuracy:", scores.mean())


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

dataFrame = pd.read_csv("student_performance_ml1.csv")
#print(dataFrame.head())

columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

x = dataFrame[columns]
y = dataFrame["FinalResult"]


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20, 
    random_state= 42
)

model = DecisionTreeClassifier(max_depth=2)

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

accuracy = accuracy_score(y_test, y_predict)
print("Accuracy", accuracy)

confMetrix = confusion_matrix(y_test, y_predict)
print("Confusion metrix :", confMetrix)
print("\nClassification Report:\n", classification_report(y_test, y_predict))


new_students = pd.DataFrame([
    [2,65,45,3,5],
    [6,88,70,7,7],
    [4,75,55,5,6]
], columns=columns)

predictions = model.predict(new_students)

print(predictions) # [0 1 0]