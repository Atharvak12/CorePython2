from writeObject import Shape
f=open("Object.ser","rb")
import pickle
s=pickle.load(f)#read object from file
print(s.color)
print(s.borderWidth)