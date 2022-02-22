#
# from abc import ABC, abstractmethod
#
#
# class Polygon(ABC):
#
#     @abstractmethod                          #body to hai nahe
#     def noofsides(self):
#         pass
#
#
# class Triangle(Polygon):
#
#     def noofsides(self):             # overriding abstract method
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#
#     def noofsides(self):                 # overriding abstract method
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#
#     def noofsides(self):                       # overriding abstract method
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#
#     def noofsides(self):                     # overriding abstract method
#         print("I have 4 sides")
#
#
#
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()
#
#
#
#
#
#
#
#


# implementation of abstract class through subclassing

import abc


class parent:
    def geeks(self):
        pass


class child(parent):
    def geeks(self):
        print("child class")


print(issubclass(child, parent))
print(isinstance(child(), parent))
