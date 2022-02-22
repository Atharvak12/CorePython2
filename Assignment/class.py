class Parent:
    def __init__(self):
        print("Hi i am parent class")


class Child(Parent):

    def me(self):
        print("Hi i am chile class")

    def set_Color(self, Color):
        self.__Color = Color

    def get_Color(self):
        return self.__Color


c = Child()
c.set_Color("Redd")
print(c.get_Color())
print(c.me())