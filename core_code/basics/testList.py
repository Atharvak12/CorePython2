l=[]
print(type(l))
#with function
l1=list([1,2,3,4,5])
print(type(l1))
l2=[1,2,3,4,5,2.3,"Rays"]
print(l2)
l3=l2+l1
print(l3)
#add a single element at the end of the list
print(l1.append(2))#append methods returns none
print(l1)
print("index of the object 1:",l1.index(1))
#add a single elemnt at specific index
l1.insert(0,"atharv")
print("index of the object 1:",l1.index(1))
print(l1)
print(len(l1))
#0      1   2   3   4   5   6   #last index=length-1
#atharv 1   2   3   4   5   2

#add multiple elements at the end of the list at same time
l1.extend([3,3,3,5])
print(l1)
l1.remove(2)#that object is going to be deleted
print(l1)
l2.clear()
print(l2)
print(l1.count(3))
#slicing[start:stop:step]
l1[0]=2#0th index value will be replaced 
print(l1)
l1[3:8:2]=[0,0,0]#3,5,7 index
print(l1)
print(l1[0])
print(l1[-5])
print(l1[0:4:2])#0,2
# l1[0]="Atharv"
print(l1.sort())
print(l1)
# l1.reverse()
print(l1)
print(l1[::-1])#start index=0-1=-1-1=-2
print("---------------------------------")
for index in range(0, len(l1)):
    print(l1[index])
print("---------------------------------")
for ele in l1:
    print(ele,end=",")