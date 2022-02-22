
# import math
# print(math.factorial(5))

# x=int(input("Enter no. you want to know factorail"))
# fact = 1
# if x < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif x == 0:
#    print("The factorial of 0 is 1")
# else:
#     for i in range(1,x+1):
#         fact = fact * i
#     print("Factotail of {} is {}".format(x,fact))






# using recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)