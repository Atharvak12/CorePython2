from shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * Shape.PI


c = Circle(2)
print("Radius = {}".format(c.get_radius()))
print("Area = {}".format(c.area()))

# s = Circle("reddd",6,4)
# s = Shape()
# s.area()
# s.get_color()

c = Shape("blue", 3, 3)
print(c.get_color())
print(c.area())     # not  possible     child not acess parrent class


