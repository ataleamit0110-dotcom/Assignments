class Arithmetic:
    def __init__(self, value1 = 0, value2 = 0):
        self.Value1 = value1
        self.Value2 = value2
    
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    # def Division(self):
    #     return self.Value1 / self.Value2

    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            return "Error! Division by zero."


obj1 = Arithmetic()
# Invoking methods for first object
obj1.Accept()
print("Addition:", obj1.Addition())
print("Subtraction:", obj1.Subtraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())

# try:
#     print("Division:", obj1.Division())
# except ZeroDivisionError:
#     print("Error! Division by zero.")