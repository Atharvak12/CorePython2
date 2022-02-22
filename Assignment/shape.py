
from abc import ABC, abstractmethod


class Shape(ABC):
    PI = 3.14  # static variable

    def __init__(self, color, width, height):
        self.__color = color  # parameterize constructor
        self.__width = width  # parameterize constructor
        self.__height = height  # parameterize constructor
        self.__circum = " "  # default constructor

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_circum(self, circum):
        self.__circum = circum

    def get_circum(self):
        return self.__circum

    @abstractmethod
    def area(self):              # abstarct method
        pass


s = Shape("red", 6, 8)
print("Color :", s.get_color())
print("Width :", s.get_width())
print("Height :", s.get_height())
s.set_circum(2)
print("Circum : ", s.get_circum())
