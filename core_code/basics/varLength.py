#variable length arguments
def addition(b,*a):
    sum=0
    for n in a:
        sum=sum+n
    return sum

res=addition(1,2,3,4,5,6,7,8)
print(res)