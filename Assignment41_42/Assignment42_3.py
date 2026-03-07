import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])   # Experience
Y = np.array([20000, 25000, 30000, 35000, 40000])  # Salary

# Train model
model = LinearRegression()
model.fit(X, Y)

# Predict salary for 6 years experience
experience = np.array([[6]])
predicted_salary = model.predict(experience)

print("Predicted Salary for 6 Years Experience: ₹", int(predicted_salary[0]))

# Plot data points
plt.scatter(X, Y)

# Plot regression line
plt.plot(X, model.predict(X))

# Labels
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction using Linear Regression")

plt.show()