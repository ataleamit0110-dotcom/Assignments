
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

def marvellousPredictor():
    #Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    # internally it will require below 4 line only. 
    # it will give us YP -> [2.8 3.2 3.6 4.  4.4]
    # Slope of line (m):  [0.4]
    # Y intercept of line :  [2.4]


    # X = np.array([[1],[2],[3],[4],[5]])
    # Y = np.array([3,4,2,4,5])
    # model = LinearRegression()
    # model.fit(X,Y)
    # pred1 = model.predict(X)



    print("values of independent variables: ", X)
    print("values of dependent variables: ", Y)

    mean_x = np.mean(X) # ([1,2,3,4,5])/5 =  3.0
    mean_y = np.mean(Y) # 3.6

    print("X Average is ", mean_x)
    print("Y Average is ", mean_y)

    n = len(X) # 5

    # y = mx + c

    # m = (summation (x -x_bar)*(y - y_bar)/ (summation (x - x_bar) ** 2 ))   //**2 meanssqaure
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)



    # m means slope
    m = numerator / denominator
    print("Slope of line (m): ", m) # 0.4

    c = mean_y - (m * mean_x)
    print("Y intercept of line : ", c) # 2.4

    x = np.linspace(1,6,n)
    y = c + m*x

    print("xxxx",x)
    print("yyyy", y)


    yPredicted = 0
    ypList = []
    for i in range(n):
        yp = m * X[i] + c
        ypList.append(yp)
        yPredicted = yPredicted + (yp - mean_y)**2
    

    print("yPredicted : ", yPredicted)
    Y_actual = 0
    for i in range(n):
        Y_actual = Y_actual + ((Y[i] - mean_y)**2)

    
    print("y - yBar ",Y_actual)
  




     

def main():
    marvellousPredictor()


if __name__ == "__main__":
    main()
