import pandas as pd
from sklearn.datasets import load_diabetes

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

data = [
    [6,148,72,35,0,33.6,0.627,50,1],
    [1,85,66,29,0,26.6,0.351,31,0],
    [8,183,64,0,0,23.3,0.672,32,1],
    [1,89,66,23,94,28.1,0.167,21,0],
    [0,137,40,35,168,43.1,2.288,33,1],
    [5,116,74,0,0,25.6,0.201,30,0],
    [3,78,50,32,88,31.0,0.248,26,1],
    [10,115,0,0,0,35.3,0.134,29,0],
    [2,197,70,45,543,30.5,0.158,53,1],
    [8,125,96,0,0,0,0.232,54,1],
    [4,110,92,0,0,37.6,0.191,30,0],
    [10,168,74,0,0,38.0,0.537,34,1],
    [10,139,80,0,0,27.1,1.441,57,0]
]

columns = [
    "Pregnancies","Glucose","BloodPressure","SkinThickness",
    "Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"
]

df = pd.DataFrame(data, columns=columns)

# print(df.head())
# print(df.info())

# print(df.isnull().sum())
# print(df.describe())

df['Outcome'].value_counts().plot(kind='bar')

# plt.title("Distribution of Diabetes Outcome")
# plt.xlabel("Outcome (0 = No, 1 = Yes)")
# plt.ylabel("Count")

# #plt.show()

# df.boxplot(figsize=(12,6))
# plt.title("Boxplot of All Features")
# plt.xticks(rotation=45)
#plt.show()

print("Glucose zeros:", (df['Glucose'] == 0).sum())
print("BloodPressure zeros:", (df['BloodPressure'] == 0).sum())

df['Glucose'] = df['Glucose'].fillna(df['Glucose'].median())
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].median())


X = df.drop("Outcome", axis=1)
y = df["Outcome"]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
print(X_scaled.head())


print(X.head())
print(y.head())

print("X shape:", X.shape)
print("y shape:", y.shape)



X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)



log_model = LogisticRegression()
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)


knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)



print("Logistic Accuracy:", accuracy_score(y_test, y_pred_log))
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))


# Logistic Regression Metrics
print("🔹 Logistic Regression")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log, zero_division=0))
print("Recall:", recall_score(y_test, y_pred_log, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred_log, zero_division=0))


# KNN Metrics
print("\n🔹 KNN")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
print("Precision:", precision_score(y_test, y_pred_knn, zero_division=0))
print("Recall:", recall_score(y_test, y_pred_knn, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred_knn, zero_division=0))


cm = confusion_matrix(y_test, y_pred_knn)

plt.imshow(cm)
plt.title("Confusion Matrix - KNN")
plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(len(cm)):
    for j in range(len(cm[0])):
        plt.text(j, i, cm[i][j], ha='center', va='center')

plt.xticks([0,1], ['No Diabetes','Diabetes'])
plt.yticks([0,1], ['No Diabetes','Diabetes'])

plt.colorbar()
plt.show()


cm = confusion_matrix(y_test, y_pred_log)

plt.imshow(cm)
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Add numbers inside boxes
for i in range(len(cm)):
    for j in range(len(cm[0])):
        plt.text(j, i, cm[i][j], ha='center', va='center')

plt.xticks([0,1], ['No Diabetes','Diabetes'])
plt.yticks([0,1], ['No Diabetes','Diabetes'])

plt.colorbar()
plt.show()