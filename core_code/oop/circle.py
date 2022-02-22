
from testConstructor import Shape
class Circle(Shape):
    def __init__(self,radius,color,border_width):
        self.__radius = radius
        super().__init__(color,border_width)
        
    def get_radius(self):
        return self.__radius
    def set_radius(self,radius):
        self.__radius = radius
    def area(self):
        print("Circl's area method")
        return self.__radius**2*Shape.PI


class Rectangle(Shape):
    def __init__(self,length,width,color,border_width):
        super().__init__(color,border_width)
        self.__length=length
        self.__width=width
    
    def get_length(self):
        return self.__length
    def set_length(self,length):
        self.__length=length
    
    def get_width(self):
        return self.__width
    
    def set_width(self,width):
        self.__width=width
        
    def area(self):
        print("Rectangle's area method")
        return self.__width*self.__length

class Triangle(Shape):
    def __init__(self,base,height,color,border_width):
        self.__base=base
        self.__height=height
        super().__init__(color,border_width)
    
    def get_base(self):
        return self.__base
    
    def set_base(self,base):
        self.__base=base
    
    def get_height(self):
        return self.__height
    
    def set_height(self,height):
        self.__height=height
        
    def area(self):
        print("Triangle's area method")
        return self.__height*self.__base*0.5
    
    