
#9 WAP which accpet number from user and return addition of digits in that number.
def sumOfDigits(num):
    total = 0
    while num != 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    return total

number = int(input("Enter a number "))
print("Sum of digits is", sumOfDigits(number))
