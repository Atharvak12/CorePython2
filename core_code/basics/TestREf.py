# def add(a, b):
#     print("a={} and b={}".format(a,b))
#     a=2
#     b=3
#     print("addition o f{} and {} is={}".format(a,b,a+b))
    
# a=4
# b=5
# print("a={} and b={}".format(a,b))
# add(a,b)
# print("a={} and b={}".format(a,b))


def add(l):
    l.append(6)
    print(l)
    
l=[1,2,3,4,5]#call by reference
print(l)
add(l)
print(l)