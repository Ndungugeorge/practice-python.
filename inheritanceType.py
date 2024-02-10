class BaseGeometry:
    def area(self):
        raise Exception ("area() is not implemented")
    def integer_validator(self,name,value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            
class Rectangle(BaseGeometry):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        self.integer_validator("width",width)
        self.integer_validator("height",height)
    def area(self):
        return self.width * self.height
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.width, self.height)
    def print(self):
        print(sel.__str__)
        
class Square(Rectangle):
    def __init__(self,size):
        self.integer_validator("size", size)
        super().__init__(size,size)
        self.__size = size

s = Square(13)

print(s)
print(s.area())