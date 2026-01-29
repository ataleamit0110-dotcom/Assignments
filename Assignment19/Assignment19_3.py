from functools import reduce

# 3 write a program which contains one list of numbers. Filter all such numbers which are greater than 70 and less than 90.
# After that increase each number by 1. Finally return product of all that numbers.

#list1 = list(input("Enter list")) #[10, 45, 70, 75, 80, 95, 100,20]
list1 = list(map(int, input("Enter list: ").split()))
#print(filteredValue(list1))
def filteredValue(value):
    if value > 70 and value < 90:
        return True
    else: return False


filteredList = list(filter(filteredValue, list1))
print(filteredList)

def mappingOnValue(value):
    return value + 1


mapList = list(map(mappingOnValue, filteredList))
print(mapList)

def reducedListFunc(no1, no2):
    return no1*no2

reducedList = reduce(reducedListFunc, mapList)
print(reducedList)
