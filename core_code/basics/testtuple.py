#tuple and list both are same 
#tuple is immutable/cannot change aftre creation
#how to create tuple
#empty tuple
t=tuple()
print(type(t))
t1=()
print(type(t1))

#with value
t2=1,2,3
print(type(t2))

t3=(1,)
print(type(t3))

l=["Aman","naman","chaman"]
l.append("Atharv")
print(type(l))
print(l)

final_guest_List=tuple(l)
print(final_guest_List)
# final_guest_List.append("Chandan")
# final_guest_List[0]="chanadan"
print(final_guest_List.index("Atharv"))
#slice[start:stop:step]
print(final_guest_List[0:4:2])#0,1
# print(final_guest_List.sort())
print(max(final_guest_List))
print(min(final_guest_List))

for e in final_guest_List:
    print(e)
    
for index in range(len(final_guest_List)):
    print(final_guest_List[index])


al=('a','b','c','d','e','f','g','h','i')
print("Max alphabet=",max(al))
