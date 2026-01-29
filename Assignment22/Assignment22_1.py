class Demo:
    no = 10
    def __init__(self,value1, value2):
        
        self.no1 = value1
        self.no2 = value2

    def fun(self):
        print("Inside fun ", self.no1, self.no2)

    def gun(self):
        print("Inside fun ", self.no1, self.no2)
        

obj1 = Demo(10,20)
obj2 = Demo(30,40)
Demo.no = 888
print("Value of class variable no from obj1:", obj1.no)
obj1.fun()
obj1.gun()
obj2.fun()
obj2.gun()