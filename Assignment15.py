numbers = [10, 20 , 30 , 40 , 55]
#squares = list(map(lambda num: num * num, numbers))

# def square(num):
#     return num * num

#squares = list(map(square, numbers))
squares = list(map(lambda num : num * num, numbers))
print(squares)


evenNos = list(filter(lambda num: num % 2 == 0, numbers))
print("list of even numbers",evenNos)