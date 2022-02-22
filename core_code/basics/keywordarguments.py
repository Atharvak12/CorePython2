# def addition(a,b):
#     print("a={}, b={}".format(a,b))
#     return a + b

# print("Sum is",addition(3,5))#relative arguments
# print("Sum is",addition(3))#Type error
# print("Sum is",addition(b=5,a=3))#keyword arguments
# # print("Sum is",addition(x=5,a=3))#keyword arguments


#Default arguments
def addition(a=5,b=5):
    print("a={},b={}".format(a,b))
    return a + b

print("Sum is:",addition())
print("Sum is:",addition(20))
print("Sum is:",addition(10,20))
