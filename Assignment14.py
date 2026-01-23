

# def square(num):
#     return num * num

square = lambda num: num * num
print("Square is:", square(5))


cube = lambda num : num * num * num
print("Cube is:", cube(3))

max = lambda no1, no2 : no1 if no1> no2 else no2
print("Greater number is:", max(10, 20))
print("Greater number is:", max(100, 20))


min = lambda num1, num2 : num1 if num1 < num2 else num2
print("Smaller number is : ", min(10, 20))
print("Smaller number is : ", min(130, 20))



isEven = lambda num : True if num % 2 == 0 else False
print("Is even:", isEven(4))
print("Is even:", isEven(7))


isOdd = lambda num : True if num % 2 == 1 else False
print("Is odd:", isOdd(5))
print("Is odd:", isOdd(6))


isdivisible = lambda num : True if num % 5 == 0 else False
print("Is divisible by 5:", isdivisible(10))


addition = lambda num1, num2 : num1 + num2
print("Addition is:", addition(10, 20))

mult = lambda num1 , num2 : num1 * num2
print("Multiplication is:", mult(10, 20))

largest = lambda num1, num2 , num3 :  num1  if (num1 > num2 and num1> num3) else  num2 if (num2 > num1 and num2 > num3) else num3
print("Largest number is:", largest(10, 20, 5))
print("Largest number is:", largest(100, 20, 5))