
#9 WAP which accpet number N numbers from user and stor it into litst. return maximum elements from that list.


def maxOfListElements(numList):
    maximum = numList[0]
    for num in numList:
        if num > maximum:
            maximum = num
    return maximum

n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)
print("Maximum element in the list is", maxOfListElements(numbers))
