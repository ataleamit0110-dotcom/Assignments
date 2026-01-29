class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def acceptRadius(self):
        self.Radius = float(input("Enter the radius of circle: "))
    
    def calculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def calculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print("Radius of Circle:", self.Radius)
        print("Area of Circle:", self.Area)
        print("Circumference of Circle:", self.Circumference)

Obj1 = Circle()
Obj2 = Circle()

# Invoking methods for first object
Obj1.acceptRadius()
Obj1.calculateArea()
Obj1.calculateCircumference()
Obj1.display()

# Invoking methods for second object
Obj2.acceptRadius()
Obj2.calculateArea()
Obj2.calculateCircumference()
Obj2.display()