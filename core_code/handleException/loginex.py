#inherit Exception class to make your custom exception class
class LoginError(Exception):
    def __init__(self,name=""):
        super().__init__("Invalid User:{}".format(name))