
# 6 write a program which accept one number from user and check whether number is positive or negative pr zero


def checkNumber(no):
    if no < 0:
        print("Negative Number")
    elif no == 0:
        print("Number is zero")
    else:
        print("Positive Number")

no = int(input("Enter number: "))
checkNumber(no)