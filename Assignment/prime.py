#
# num = 29
# flag = False
# if num > 1:
#     for i in range(2, num):                                   #factor check
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")
#
#

#
# num = int(input("check no is primr or not"))
# if num > 1:
#     for i in range(2, num):                                          # check for factors
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")




#all prime list
lower = 1
upper = 100
c=0
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:                         # all prime numbers must be  greater than 1
        for i in range(2, num):
            if (num % i) == 0:           #
                break
        else:
            print(num ,end=" ")