
# 3 write a program which contains one list of numbers. Filter all such numbers which are prime.
# After that multiple each number by 2. Finally return maximum number from all.
from functools import reduce


list1 = list(map(int, input("Enter list: ").split()))
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def multiplyByTwo(value):
    return value * 2

def maxNumber(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2
    
filteredValues = list(filter(isPrime, list1))
print("Filtered Prime Numbers:", filteredValues)
mapValues = list(map(multiplyByTwo, filteredValues))
print("Mapped Values (Multiplied by 2):", mapValues)
maxValue = reduce(maxNumber, mapValues)
print("Maximum Value:", maxValue)
