
from shape import Shape


class Triangle(Shape):

    def __init__(self, base, height ,color ) :
        # super(Rectangle, self).__init__(length, breath)

        self.__base  = base
        self.__height = height
        # self.__color = color
        super().__init__(color)

    def set_base(self, base):
        self.__base = base

    def get_base(self):
        return self.__base

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def area(self):
        return self.__base * self.__height * 0.5


t = Triangle(2,2)
print("Base  = {}".format(t.get_base()))
print("Height = {}".format(t.get_height()))
print("Area = {}".format(t.area()))

t = Shape(9,3,"eds")
print("Color :", s.get_color())
print("Width :", s.get_width())
print("Height :", s.get_height())
s.set_circum(2)
print("Circum : ", s.get_circum())
