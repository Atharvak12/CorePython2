class Shape(object):
    def __init__(self,c,bw):
        self.color=c
        self.borderWidth=bw
    
    def get_color(self):
        return self.color
    
    def get_borderWidth(self):
        return self.borderWidth
    
s=Shape("REd",2)
import pickle
f=open("Object.ser",'wb')
pickle.dump(s,f)#object saved into the fileh
f.close()
print("Object saved into file")