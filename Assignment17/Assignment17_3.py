
#3 . arite a program which accpet one number from user and return its factorial.
def factorial(num):
    if num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result = result * i
        return result

number = int(input("Enter a number "))
print("Factorial is", factorial(number))