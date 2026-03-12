import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([50,55,60,65,70])

model = LinearRegression()
model.fit(x,y)

print("Coefficient: ", model.coef_)

print("Intercept ", model.intercept_)
prediction = model.predict([[6]])
print(prediction)
#Marks=5×StudyHours+45
#5×6+45