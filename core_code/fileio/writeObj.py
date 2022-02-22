class Shape:
    def __init__(self,color,bw):
        self.color = color
        self.borderWidth =bw
    def getColor(self):
        return self.color
    def getBorderWidth(self):
        return self.borderWidth
    

import pickle
shape=Shape("Red",8)
f1=open("Object.ser","wb")
pickle.dump(shape,f1)#write serialized object to the file
f1.close()
print("Object Saved")

#read the object from the file
f2=open("Object.ser","rb")
sh=pickle.load(f2)#binarey to object/deserialzed
print("Color:",sh.getColor()) 
print("Bw:",sh.getBorderWidth())
f2.close()

