
#3 . arite a program which accpet one number from user and return addition of its factors.
def sumOfFactors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total = total + i
    return total
number = int(input("Enter a number "))
print("Sum of factors is", sumOfFactors(number))