
num = int(input("Enter the no.: \n"))
# print(str(num)[::-1])
#

a=0
#num =123
while num != 0:
    digit = num % 10
    a = (a*10)+digit
    num =  num // 10
print(a)