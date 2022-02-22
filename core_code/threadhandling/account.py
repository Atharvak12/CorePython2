from re import S
from time import sleep
import threading
class Account:
    def __init__(self):
        self.__lock=threading.Lock()
        self.__balance=0
    
    def getbalance(self):
        sleep(1)
        return self.__balance
    
    def setbalance(self,bal):
        sleep(1)
        self.__balance=bal
    
    def deposit(self,amount):
        #get the lock
        self.__lock.acquire()
        cb=self.getbalance()
        self.setbalance(amount+cb)
        self.__lock.release()
        


