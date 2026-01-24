
# 6 write a program which accept one number from user and check whether number is divisible by 5 or not


def divisbleByFive(no):
    if no % 5 == 0:
        return True
    else:
        return False

no = int(input("Enter number: "))
result = divisbleByFive(no)
if result:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")