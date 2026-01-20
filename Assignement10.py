# 1 WAP which accpets one number and print multiplication table of that number

def multiplicationTable(num):
    for index in range(1, 11):
        print(index * num)
        
multiplicationTable(4)

# 2  WAP which accpets one number and print sum of first n natural numbers
def sumOfNaturalNumbers(num):
    sum = 0
    for index in range(1,num+1):
        sum = sum + index
    
    return sum

# 3 WAP which accpets one number and print factorial of that number
result = sumOfNaturalNumbers(5)
print("Sum of first n natural numbers is:", result)


def factorial(num):
    fact = 1
    for no in range (num,1,-1):
        print(no)
        fact = fact * no 
    return fact

result = factorial(5)
print("Factorial is:", result)



# 4 WAP which accpets one number and print all even numbers till that number
def printEvenNumbers(num):
    for index in range(2,num+1,2):
        print(index)

printEvenNumbers(10)


#5 # 4 WAP which accpets one number and print all odd numbers till that number
def printOddNumbers(num):
    for index in range(1,  num+1,2):
        print(index)

printOddNumbers(10)

    
