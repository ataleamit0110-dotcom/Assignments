# 4 WAP which accpets one number and checks whether it is prime

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
if isPrime(11):
    print("Number is Prime")
else:
    print("Number Not Prime")
 
 # 4 WAP which accpets one number and count total digits in that number
# 3421
# count 4
def countDigitt(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    print("Total digit ",count)

countDigitt(3421)
    
 # 4 WAP which accpets one number and print sum of that digits
def sumOfDigits(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num // 10 # double slash is for print integer value ans single print float value
    return sum

print("Sum of digits:", sumOfDigits(3421))

# 5 WAP which accpets one number and print reverse of that number
def reverse(num):
    rev = 0
    while num >0 :
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev

print("Reversed number is:", reverse(3421))


# 5 WAP which accpets one number and check whether that number is palindrome or not

def isPalindrome(num):
    revNo =  reverse(num)
    if revNo == num:
        return
    else:
        return False

if isPalindrome(1221):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

