from circle import *
c=Circle(3,"REd",3)
cl=c.get_color()
bw=c.get_borderwidth()
r=c.get_radius()
ar=c.area()
print("Color:{}\nBW={}\nRadius={}\nArea={}".format(cl,bw,r,ar))
print("--------------------------------------")

r=Rectangle(3,4,"Black",4)
cl=r.get_color()
l=r.get_length()
w=r.get_width()
bw=r.get_borderwidth()
a=r.area()
print("Color:{}\nBW={}\nlength={}\nwidth={}\narea={}".format(cl,bw,l,w,a))

print("---------------------------------------")
t=Triangle(2,4,"White",3);
cl=t.get_color()
bw=t.get_borderwidth()
b=t.get_base()
h=t.get_height()
a=t.area()

print("Color:{}\nBW={}\nBase={}\nHeight={}\narea={}".format(cl,bw,b,h,a))