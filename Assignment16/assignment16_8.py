


# 8 write a program which accept one number from user and print that number of * on screen
def dispalyStar(no):
    for i in range(no):
        print("*", end=" ")

no = int(input("Enter number: "))
dispalyStar(no)