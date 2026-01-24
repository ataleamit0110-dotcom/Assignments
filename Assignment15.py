from functools import reduce
#squares = list(map(lambda num: num * num, numbers))

# def square(num):
#     return num * num

#squares = list(map(square, numbers))
numbers = [10, 20 , 30 , 40 , 55,33]


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

# 5     write a lambda function using reduce() which accepts list of numbers and return maximum element
maximum = reduce(lambda num1, num2 : num1 if num1 > num2 else num2, numbers)    
print("maximum element is:", maximum)

# 6  write a lambda function using reduce() which accepts list of numbers and return minimum element
minimun = reduce(lambda num1, num2 : num1 if num1 < num2 else num2, numbers)
print("Minimum elemnet is: ", minimun)

# 7 write a lambda function using filter() which accepts list of strings and return list of strings having length greater than 5
strList = ["AMIT", "SAISHA", "SACHIN", "TENDULAKR", "MS DHONI"]
filteredString = filter(lambda str: len(str) > 5, strList)
print("filteredString is ", list(filteredString))

# 8 write a lambda function using filter() which accepts list of numbers and return list of numbers which are divisible by 3 and 5
divByThreeAndFive = filter(lambda no: no % 3 ==0 and no % 5 == 0, numbers)
print("List which is idivisible by 3 and 5", list(divByThreeAndFive))

# 9 write a lambda function using reduce() which accepts list of numbers and return product of all numbers
product = reduce(lambda num1, num2: num1 * num2, numbers)
print("Product of list :", product)


#10 write a lambda function using reduce() which accepts list of numbers and return count of even numbers

countOfEven = reduce(lambda count, num: count + 1 if num % 2 == 0 else count, numbers, 0)
print("Count of even:", countOfEven)
# countOfEven = reduce(lambda count = count + 1 if num%2 == 0, numbers)
