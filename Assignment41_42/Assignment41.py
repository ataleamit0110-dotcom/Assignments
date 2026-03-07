# [A,B,C,D]
# x = [1,2,3,5]
# Y = [2,3,1,6]
# [R, R, B, B] 
# i.e Red Blue

# Predict (3,3) -> ?

import numpy as np
import math


def eucDistance(p1,p2):
    ans = math.sqrt((p1['X']- p2['X']) ** 2 + (p1['Y'] - p2['Y']) **2)
    return ans
    


def MarvellousKNeighboursClassifier():
    border = "-"*40
    data = [{'point': 'A','X':1,'Y':2,'label': 'Red'},
            {'point': 'B','X':2,'Y':3,'label': 'Red'},
            {'point': 'C','X':3,'Y':1,'label': 'Blue'},
            {'point': 'D','X':5,'Y':6,'label': 'Blue'}]
    
    print(border)
    print("Marvellous Used defined KNN")
    print(border)
    
    print(border)
    print("Training data set")
    print(border)

    for i in data:
        print(i)
    

    print(border)
    input1 = int(input("enter 1st co ordinate form user "))
    input2 = int(input("enter 1st co ordinate form user "))

    new_point = {'X': input1, 'Y':input2}

    # calculate all distances 

    for d in data:
        d['distance'] = eucDistance(d, new_point)
    
    print(border)
    print("Calculated distances are : ")
    print(border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key= lambda item : item['distance'])
    print(border)
    print("sorted data is ")
    for d in sorted_data:
        print(d)
    
    k = 3
    nearest = sorted_data[:k]  # first 3
    print(border)
    print("nearesr 3 elemnets are :")
    print(border)
    for d in nearest:
        print(d)


    # voting (majority)
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1
    
    print(border)
    print("voting result")
    print(border)

    for d in votes:
        print("Name ", d, "Number of votes : ", votes[d])

    print(border)

    predicted_class = max(votes, key= votes.get)
    print("Predicted class of (3,3) is ", predicted_class)
    print(border)

    


    
    



def main():
    MarvellousKNeighboursClassifier()



if __name__ == "__main__":
    main()