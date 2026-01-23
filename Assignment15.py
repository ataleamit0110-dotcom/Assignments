from functools import reduce
#squares = list(map(lambda num: num * num, numbers))

# def square(num):
#     return num * num

#squares = list(map(square, numbers))
numbers = [10, 20 , 30 , 40 , 55]


# 1 write a lambda function using map() which accepts list of numbers and return list of square of each number
squares = list(map(lambda num : num * num, numbers))
print("list of squares:", squares)


# 2 write a lambda function using filter() which accepts list of numbers and return list even numbers
evenNos = list(filter(lambda num: num % 2 == 0, numbers))
print("list of even numbers",evenNos)

# 3 write a lambda function using map() which accepts list of numbers and return list of odd numbers
oddNo = list(map(lambda num : num % 2 == 1, numbers))
print("list of odd numbers", oddNo)

# 4     write a lambda function using reduce() which accepts list of numbers and return addition of all numbers
addition = reduce(lambda num1, num2 : num1 + num2, numbers)
print("addition of all numbers", addition)