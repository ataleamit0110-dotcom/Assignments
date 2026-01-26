
#9 WAP which accpet number from user and return number of digits in that number.

def countDigits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

number = int(input("Enter a number "))
print("Number of digits is", countDigits(number))