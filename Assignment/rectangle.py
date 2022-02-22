from shape import Shape


class Rectangle(Shape):

    def __init__(self, length, breath) :
        # super(Rectangle, self).__init__(length, breath)

        self.__length = length
        self.__breath = breath
        # self.__color = color

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_breath(self, breath):
        self.__breath = breath

    def get_breath(self):
        return self.__breath

    def area(self):
        return self.__length * self.__breath


r = Rectangle(2,2)
print("Length  = {}".format(r.get_length()))
print("Breath = {}".format(r.get_breath()))
print("Area = {}".format(r.area()))

#
# r = Shape("blue", 3, 3)
# r.area()
# print(r.get_color())
