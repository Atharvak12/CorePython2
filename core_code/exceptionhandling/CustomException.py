class LoginError(Exception):
    def __init__(self,username):
        super().__init__("Invalid User:{}".format(username))