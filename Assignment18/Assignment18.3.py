
#9 WAP which accpet number N numbers from user and store it into litst. return minimum elements from that list.
def minOfListElements(numList):
    minimum = numList[0]
    for num in numList:
        if num < minimum:
            minimum = num
    return minimum

n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)
print("Maximum element in the list is", minOfListElements(numbers))
