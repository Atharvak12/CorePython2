from loginex import LoginError

def validateUser( username="", password=""):
    if(username.__eq__("Admin") and password.__eq__("pass1234")):
        print("Welcome :",username)
    else:
        raise LoginError(username)


#call the funtion
try:
    validateUser("Ad",'pass1234')
except LoginError as e:
    print("Error Message:",e)