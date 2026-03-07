# [A,B,C,D]
# x = [1,2,3,5]
# Y = [2,3,1,6]
# [R, R, B, B] 
# i.e Red Blue

# Predict (3,3) -> ?

import numpy as np
import math


def eucDistance(p1,p2):
    ans = math.sqrt((p1['Study Hours']- p2['Study Hours']) ** 2 + (p1['Attendance'] - p2['Attendance']) **2)
    return ans
    


def MarvellousKNeighboursClassifier():
    border = "-"*40
    data = [{'Study Hours': 2,'Attendance':60,'Result': 'Fail'},
            {'Study Hours': 5,'Attendance':80,'Result': 'Pass'},
            {'Study Hours': 6,'Attendance':85,'Result': 'Pass'},
            {'Study Hours': 1,'Attendance':50,'Result': 'Fail'}]


    input1 = int(input("enter Study hours form user "))
    input2 = int(input("enter attendance form user "))

    new_point = {'Study Hours': input1, 'Attendance':input2}

    # calculate all distances 

    for d in data:
        d['distance'] = eucDistance(d, new_point)
    
    print("Calculated distances are : ")

    for d in data:
        print(d)

    sorted_data = sorted(data, key= lambda item : item['distance'])
    print("sorted data is ")
    for d in sorted_data:
        print(d)
    
    k = 3
    nearest = sorted_data[:k]  # first 3
    print("nearesr 3 elemnets are :")
    for d in nearest:
        print(d)


    # voting (majority)
    votes = {}
    for neighbour in nearest:
        label = neighbour['Result']
        votes[label] = votes.get(label,0) + 1
    
    print(border)
    print("voting result")
    print(border)

    for d in votes:
        print("Name ", d, "Number of votes : ", votes[d])

    print(border)

    predicted_class = max(votes, key= votes.get)
    print("Predicted class is ", predicted_class)
    print(border)

    


    
    



def main():
    MarvellousKNeighboursClassifier()



if __name__ == "__main__":
    main()