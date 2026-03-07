import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# step 1 load dataset

dataSetPath = "student_performance_ml.csv"
df = pd.read_csv(dataSetPath)
print("First 5 rows",df.head())
print("last 5 rows\n",df.tail())
print("Shape of dataset - Total number of rows and columns\n",df.shape)
print("Columns in dataset\n",df.columns)
print("Data types of each column\n",df.dtypes)


feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]
X = df[feature_cols]
Y = df["FinalResult"]
print("X shape ", X.shape)
print("Y Shape ", Y.shape)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier()

model.fit(X_train, Y_train)

yPredicted = model.predict(X_test)
accuracy = accuracy_score(Y_test, yPredicted)
print("accuracy ", accuracy)

conf_metrix = confusion_matrix(Y_test, yPredicted)
print("Confusion metrix", conf_metrix)

# Q 5 calculate training accuracy and testing accurcay. 
# check model is overlifting or underlifting 

y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(Y_train,y_train_pred)
print("Training Accuracy:", train_accuracy) # 1
# no overliftingh


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

depth_values = [1, 3, None]

for depth in depth_values:
    print("\n==============================")
    print("Model with max_depth =", depth)

    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, Y_train)

    # Training Accuracy
    train_pred = model.predict(X_train)
    train_acc = accuracy_score(Y_train, train_pred)

    # Testing Accuracy
    test_pred = model.predict(X_test)
    test_acc = accuracy_score(Y_test, test_pred)

    print("Training Accuracy:", train_acc)
    print("Testing Accuracy :", test_acc)

# Model with max_depth = 1
# Training Accuracy: 1.0
# Testing Accuracy : 1.0

# ==============================
# Model with max_depth = 3
# Training Accuracy: 1.0
# Testing Accuracy : 1.0

# ==============================
# Model with max_depth = None
# Training Accuracy: 1.0
# Testing Accuracy : 1.0


# 7 use the trained model to predict result for student with. 
# study hours - 6, attendance 85, previous score 66, assignment completed 7, sleep hours 7 .
#  will student pass or fail

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [96],
    "AssignmentsCompleted": [7],
    "SleepHours": [4]
})
prediction = model.predict(new_student)
if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")
