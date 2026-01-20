#1 WAP to accept one char and ceck whether that char is vowel or not
#Input  a
# Output vowel

def checkVowels(ch):
    #vowels = "aeiou"
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return True
    else:
        return False
    # if vowels.__contains__(ch.lower()):
    #     return True
    # else:
    #     return False
    
result = checkVowels('a')
print("Is vowel:", result)

# 2 WAP which accept 1 number and it print its factors
def printFactors(no):
    for i in range(1, no+1):
        if no % i == 0:
            print("factors are ",i)

printFactors(12)

# 3.WAP which accept 2 nos and print addition, multiplication, division and subtraction of that nos
def arithmeticOperations(no1, no2):
    addition = no1 + no2
    subtraction = no1 - no2
    multiplication = no1 * no2
    division = no1 / no2
    return addition, subtraction, multiplication, division

add, sub, mul, div = arithmeticOperations(10, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

#4 def print 1 to n nos
def printNos(no):
    for value in range(1, no+1):
        print(value)

printNos(10)

#5 def print 1 to n in reverse
def printNosReverse(no):
    for value in range(no, 0, -1):
        print(value)

printNosReverse(10)