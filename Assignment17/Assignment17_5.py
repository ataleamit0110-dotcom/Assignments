
#3 . arite a program which accpet one number from userand check number is prime or not.
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number "))
if isPrime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
