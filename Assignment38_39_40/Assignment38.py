from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# step 1 load dataset

dataSetPath = "student_performance_ml.csv"
df = pd.read_csv(dataSetPath)
print("First 5 rows",df.head())
print("last 5 rows\n",df.tail())
print("Shape of dataset - Total number of rows and columns\n",df.shape)
print("Columns in dataset\n",df.columns)
print("Data types of each column\n",df.dtypes)


# Q 2
print("Total number of students in dataset\n",df['FinalResult'].count())
print("student result",df["FinalResult"])
print("Students failed in exame", len(df[df["FinalResult"] == 0]))
print("Students passed in exame", df["FinalResult"].value_counts()[1])

# Q 3 :
print("average studyhours :", df["StudyHours"].mean())
print("average of attendance", df["Attendance"].mean())
print("Maximum PreviousScore", df["PreviousScore"].max())

print("Minumum sleep hours", df["SleepHours"].min())

#StudyHours,Attendance,PreviousScore,AssignmentsCompleted,SleepHours,FinalResult


#4  use value_count() to analyse the distribution of final result . 
# calculate the percentage of pass and fail student. is the dataset balanced?
resultCount = df["FinalResult"].value_counts()
print("Final Result Distribution:\n", resultCount)

#  FinalResult
# 1    18
# 0    12

totalStudents = len(df)
passPecentage = (resultCount[1] / totalStudents) * 100

failPercentage = (resultCount[0] / totalStudents) * 100
print(f"Pass Percentage: {passPecentage:.2f}%")
print(f"Fail Percentage: {failPercentage:.2f}%")

avgStudy = df.groupby("FinalResult")["StudyHours"].mean()
print("Average Study Hours:\n", avgStudy)


avgAttendance = df.groupby("FinalResult")["Attendance"].mean()
print("Average Attendance:\n", avgAttendance)

# Average Study Hours:
#  FinalResult
# 0    2.550000
# 1    6.372222

#So average StudyHours for passed will be much higher.
    
# Name: StudyHours, dtype: float64
# Average Attendance:
#  FinalResult
# 0    67.750000
# 1    86.611111

# attendance also clearly higher for passed students.


# 6

# plt.hist(df["StudyHours"], bins=8)
# plt.xlabel("Study Hours")
# plt.ylabel("Number of Students")
# plt.title("Distribution of Study Hours")
# plt.show()

# plt.hist(df[df["FinalResult"] == 0]["StudyHours"], alpha=0.5, label="Failed")
# plt.hist(df[df["FinalResult"] == 1]["StudyHours"], alpha=0.5, label="Passed")

# plt.xlabel("Study Hours")
# plt.ylabel("Number of Students")
# plt.legend()
# plt.show()


# 7

# Scatter plot
plt.scatter(df["StudyHours"], df["PreviousScore"])

# Regression line
x = df["StudyHours"]
y = df["PreviousScore"]

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")

plt.show()

# Correlation
print("Correlation:", df["StudyHours"].corr(df["PreviousScore"]))



# -----------------------
plt.figure()
plt.boxplot(df["Attendance"])
plt.title("Box Plot of Attendance")
plt.ylabel("Attendance")
plt.show()

# -----------------------
# Outlier Detection (IQR)
# -----------------------
Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Attendance"] < lower_bound) | 
              (df["Attendance"] > upper_bound)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

if outliers.empty:
    print("\nNo Outliers Found")
else:
    print("\nOutliers:\n", outliers)

    # Scatter Plot
plt.figure()
plt.scatter(df["SleepHours"], df["FinalResult"])

plt.xlabel("Sleep Hours")
plt.ylabel("Final Result (0 = Fail, 1 = Pass)")
plt.title("Sleep Hours vs Final Result")

plt.show()