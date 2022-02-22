from CustomException import LoginError
def validate(un, pwd):
    if(un.__eq__("Admin") and pwd.__eq__("Pass1234")):
        print("Welcome user ",un)
    else:
        try:
            raise LoginError(un)#raise custom exception
        except LoginError as e:
            print(e)

#call the function
validate("Admin","Pass1234")