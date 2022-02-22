from shape import Shape
#create an object
s=Shape()
s.set_color("Red")
s.set_border_width(3)
print("color:",s.get_color())
print("border width:",s.get_border_width())
print(s.PI)
print(Shape.PI)
print(id(s))

print("------------------------------------------")
s1=Shape()
s1.set_color("White")
s1.set_border_width(5)
print("color:",s1.get_color())
print("border width:",s1.get_border_width())
print(s1.PI)
print(Shape.getPi())
print(id(s1))
# del s1
print(Shape.__dict__)