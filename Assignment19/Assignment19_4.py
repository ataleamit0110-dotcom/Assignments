
# 3 write a program which contains one list of numbers. Filter all such numbers which are even.
# After that square each number. Finally return addition of all that numbers.
from functools import reduce

list1 = list(map(int, input("Enter list: ").split()))

def squareOfValue(value):
    return value*value

def filteredValue(value):
    if value % 2 == 0:
        return True
    else:
        return False

def additionOfAll(value1,value2):
    return value1 + value2

filteredValues = list(filter(filteredValue, list1))
print(filteredValues)

mapValues = list(map(squareOfValue,filteredValues))
print(mapValues)

addValues = reduce(additionOfAll, mapValues)
print(addValues)