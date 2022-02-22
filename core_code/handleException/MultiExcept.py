try:
    a=int(input("Enter 1st no\n"))
    b=int(input("Enter 2nd no\n"))
    div=a/b
    print("Div of {} and {} is {}".format(a,b,div))
except ZeroDivisionError as x:
    print("Please enter Divisor greater than 0")
except ValueError as y:
    print("Please enter a Number")
