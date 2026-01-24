#2 write a program which contains one function named as checkNum which accept one number and print whether number is even or odd
def checkNum(no):
    if no % 2 == 0:
        return True
    else:
        return False

result = checkNum(10)
if result:
    print("Even Number")
else:
    print("Odd Number")