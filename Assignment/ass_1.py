
x = int(input("Enter first no : \n"))
y = int(input("Enter secound no: \n"))

if (x>y) :
    print("First no. {} is greater then secound no {} by {} ".format(x,y,(x-y)))
elif x==y :
    print("First no. {} and secound no {} are Equal ".format(x, y))
else:
    print("Secound  no. {} is greater then first no {} by {} ".format(y, x, ( y-x)))
