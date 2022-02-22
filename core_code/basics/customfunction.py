#types of functions
#1. Keyword arguments
#2. Relative arguments
#3. default arguments
#4. variable length arguments

#Relative arguments
#1. without return type
def addition(a,b):
    sum=a+b
    print("Sum of {} and {} is ={} ".format(a,b,sum))
    return#without value

#call the function
# print(addition(2,3))


#2. WIth return type
# def addition(a,b):
#     sum=a+b
#     return sum      #with value

def addition1(a,b):
    print("a={},b={}".format(a,b))
    return a+b      #with value

#call the function
res=addition1(4,5)
print("SUm is:",res)


