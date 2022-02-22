import threading
from account import Account

class RaceCondition(threading.Thread):
    #class var
    account=Account()
    
    
    def __init__(self,name):
        super().__init__()
        self.__name = name
    
    def run(self):
        for i in range(1,6):
            RaceCondition.account.deposit(100)
            print("{} final balance is {}".format(self.__name,RaceCondition.account.getbalance()))
    


t1=RaceCondition("AJay")
t2=RaceCondition("Vijay")

t1.start()
t2.start()

t1.join()

    
