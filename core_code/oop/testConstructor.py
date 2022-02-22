from abc import ABC,abstractmethod
class Shape(ABC):
    PI=3.14
    def __init__(self,color,bw):
        self.__color = color
        self.__borderwidth = bw
    
    def set_borderwidth(self,bw):
        self.__borderwidth = bw
    
    def get_borderwidth(self):
        return self.__borderwidth
    
    def set_color(self,color):
        self.__color = color
    
    def get_color(self):
        return self.__color
    
    @abstractmethod
    def area(self):
        pass


#test
# s=Shape("Red",3)
# print(s.get_color())
# print(s.get_borderwidth())
