
#
# a=int(input("Enter the terms : "))
# f=0
# s=1
# if a<=0:
#     print("The requested series is",f)
# else:
#     print(f,s,end=" ")
#     for x in range(2,a):
#         next=f+s
#         print(next,end=" ")
#         f=s
#         s=next


#recursion
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
x = int(input("Enter the terms: "))
if x <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(x):
        print(fibo(i))