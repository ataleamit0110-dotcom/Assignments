
# 1 WAP which contain one function named as dispaly() that print "Jay Ganesg"

def display():
    print("Jay Ganesg")


display()


# 2. WAP which contain one function named checkkGreater () that accept two numbers print greater number.
def checkkGreater(no1, no2):
    if no1 > no2 :
       return no1
    else:
       return no2
    
result = checkkGreater(10, 20)
print("Greater number is:", result)

# 3.  WAP which accepts one number and print square of that number

def square(num):
    return num * num
result = square(5)
print("Square is:", result)

# 4. WAP which accepts one number and prints cube of that number
def cube(num):
    return num * num * num  
result = cube(3)
print("Cube is:", result)

# 5. WAP which accepts one number and check whather it is divisible by 3 and 5.
def checkDivisible(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False
    
result = checkDivisible(15)
print("Is divisible by 3 and 5:", result)