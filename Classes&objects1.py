class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()
print("Area:", area)
