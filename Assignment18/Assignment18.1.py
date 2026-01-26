
#9 WAP which accpet number N numbers from user and stor it into litst. return addition of elements from that list.
def sumOfListElements(numList):
    total = 0
    for num in numList:
        total += num
    return total

n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)
print("Sum of list elements is", sumOfListElements(numbers))
