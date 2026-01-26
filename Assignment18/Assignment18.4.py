
#9 WAP which accpet number N numbers from user and store it into litst. take 1 more elemnet and count frequnecy of that number
def frequencyOfNum(numList,no):
    freq = 0
    for num in numList:
        if num == no:
            freq = freq +1
    return freq

n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)

number = int(input("Enter number to check frequency: "))
print("Frequency is", frequencyOfNum(numbers,number))

