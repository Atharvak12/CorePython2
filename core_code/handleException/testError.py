try:
    a=int(input("Enter 1st no\n"))
    b=int(input("Enter 2nd no\n"))
    div=a/b
    print("Div of {} and {} is {}".format(a,b,div))
except Exception as x:
    print("Error Msg:",x)
else:
    print("Successful Executed")
finally:
    print("I am In finally")