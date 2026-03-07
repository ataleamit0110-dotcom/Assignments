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

# Q 1
# display important score of each feature 
# which feature is contributed the most in predicting result 
# which feature contribute the least

# Get feature importance
importance = model.feature_importances_

# Create DataFrame
feature_importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance": importance
})

# Sort descending
feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)

print(feature_importance_df)

#                 Feature  Importance
# 0            StudyHours         1.0
# 1            Attendance         0.0
# 2         PreviousScore         0.0
# 3  AssignmentsCompleted         0.0
# 4            SleepHours         0.0


# 2
# remove the sleep hours from dataset 
# and train the model
# compare new accuracy with prev accurcavy
# does removing the feture affect the performance?

# Remove SleepHours
feature_cols_reduced = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X_reduced = df[feature_cols_reduced]

X_train_r, X_test_r, Y_train_r, Y_test_r = train_test_split(
    X_reduced, Y, test_size=0.2, random_state=42
)

model_reduced = DecisionTreeClassifier(max_depth=3, random_state=42)
model_reduced.fit(X_train_r, Y_train_r)

train_acc_reduced = accuracy_score(Y_train_r, model_reduced.predict(X_train_r))
test_acc_reduced = accuracy_score(Y_test_r, model_reduced.predict(X_test_r))

print("\nWithout SleepHours")
print("Training Accuracy:", train_acc_reduced) #1.0
print("Testing Accuracy :", test_acc_reduced)# 1.0

#NO

# SleepHours was not strong predictor
# StudyHours + Attendance already decide PASS/FAIL


# Q3
# train the model using study hours and attendance
# compare the accuracy withe the full feature model. 
# is the model still performing well? -> ans Yes

feature_cols_minimal = [
    "StudyHours",
    "Attendance"
]

X_minimal = df[feature_cols_minimal]

X_train_m, X_test_m, Y_train_m, Y_test_m = train_test_split(
    X_minimal, Y, test_size=0.2, random_state=42
)

model_minimal = DecisionTreeClassifier(max_depth=3, random_state=42)
model_minimal.fit(X_train_m, Y_train_m)

train_acc_min = accuracy_score(Y_train_m, model_minimal.predict(X_train_m))

print("\nMinimal Feature Model (StudyHours + Attendance)")
print("Training Accuracy:", train_acc_min) # 1.0

# !4
# create new data frame for 5 studets and use the trained model and
#  predict result. display predictions 


# Create new students
new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 7, 3],
    "Attendance": [65, 75, 85, 92, 70],
    "PreviousScore": [45, 55, 66, 72, 50],
    "AssignmentsCompleted": [3, 5, 7, 8, 4],
    "SleepHours": [5, 6, 7, 8, 6]
})

print("New Students Data:")
print(new_students)
# Predict
predictions = model.predict(new_students)

# Add prediction column
new_students["PredictedResult"] = predictions

# Convert 0/1 to Fail/Pass
new_students["PredictedResult"] = new_students["PredictedResult"].map({0: "Fail", 1: "Pass"})

print("\nPredictions:")
print(new_students)