
class Shape:
    "Shape Related info"
    #class variable
    PI=3.14 #static
    
    #constructor
    def __init__(self):
        #instance variable
        self.__color=""
        self.__borderwidth=0
    #instance method
    def set_color(self,c):
        self.__color=c
    def get_color(self):
        return self.__color
    
    def set_border_width(self,bw):
        self.__borderwidth=bw
    
    def get_border_width(self):
        return self.__borderwidth
    
    def getPi():
        return Shape.PI
    
    def __del__(self):
        print("Object Deleted {}".format(self.__class__.__name__))
    
    def __str__(self):
        return "color={} bw={}".format(self.__color,self.__borderwidth)

