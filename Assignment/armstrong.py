#
# num = 1634  # 153
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** order
#     temp //= 10
#
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


# list of armstrom
lower = 100
upper = 2000
for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp //= 10
    if num == sum:
        print(num)
