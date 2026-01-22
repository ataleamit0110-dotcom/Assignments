# 1 WAP which accepts length and width of rectangle and print area of rectangle
def calculate_area(length, width):
    return length * width

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
area = calculate_area(l, w)
print("Area of rectangle is:", area)

# 2 WAP which accepts radius of circle and print area of circle
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

r = float(input("Enter radius of circle: "))
area = area_of_circle(r)
print("Area of circle is:", area)

# 3 WAP which accepts one number and check whether that number is perfect number or not
def isPerfectNo(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum = sum + i 
            print(sum)
            if sum == number:
                return True
            else:
                return False
    
if isPerfectNo(6):
    print("Number is perfect")
else:
    print("Number is Not perfect")


# 4 WAP which accepts one number and print its binary equivalent
def printBinary(num):
    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print(binary)

n = int(input("Enter a number: "))
printBinary(n)

# 5 WAP which accepts marks of student and print result as Distinction, First Class, Second Class, Fail
def display_result(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"


marks = int(input("Enter marks: "))
result = display_result(marks)
print("Result:", result)