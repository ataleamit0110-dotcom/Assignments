
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
