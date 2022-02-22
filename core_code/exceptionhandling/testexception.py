#multiple assignement
a=int(input("Enter the number\n"))
b=int(input("Enter another no\n"))
try:
    div=a/b
    print("Div of {} and {} is ={}".format(a,b,div))
except ZeroDivisionError as e:
    # print("PLease enter the denometer rather than 0")
    #exception message
    print("Error:",e)
else:
    print("program exceuted successfully")
finally:
    print("in finally block")

