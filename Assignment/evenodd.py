# x = int( input("Enter a num :"))
# if x % 2 == 0 :
#     print("Even ")
# else:
#     print("Odd")

#

# #eeven - odd number
# x = input("neter no ").strip()
# even = 0
# odd = 0
# for i in x:
#     if int(i) % 2 == 0:
#         even = even + int(i)
#     else:
#         odd = odd + int(i)
# print(even - odd)



#
# a = []
# n = int(input("Enter number of elements:"))
# for i in range(1, n + 1):
#     b = int(input("Enter element:"))
#     a.append(b)
# even = []
# odd = []
#
# for j in a:
#     if (j % 2 == 0):
#         a = even.append(j)
#     else:
#         b = odd.append(j)
#
# print("The even list", even)
# print("The odd list", odd)
# print(int(b - a ))

c,d = 0,0

for j in range(2, 11, 2 ):      # 2,4,6,8,10
    c += j
print(c)

for i in range(1, 11, 2):      # 1,3,5,7,9
    d += i
print(d)

print(c-d)