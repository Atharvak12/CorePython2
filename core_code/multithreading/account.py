from time import sleep
import threading
class Account:
    def __init__(self):
        #create a lock for synchronized access
        self.lock = threading.Lock()#crreate an instance of Lock
        self.balance =0
    
    def set_balance(self,balance):
        sleep(1)
        self.balance = balance
    
    def get_balance(self):
        sleep(1)
        return self.balance
    
    def deposit(self,amount):
        self.lock.acquire()#enter in critical section and perform the task
        bal=self.get_balance()
        self.set_balance(bal+amount)
        self.lock.release()# after finishing the task release the lock


from threading import Thread
class RaceCondition(Thread):
    account=Account()#will get one time meory for whole class
    
    def __init__(self,name):
        super().__init__()
        self.name=name
    
    def run(self):
        for i in range(1,6):
            RaceCondition.account.deposit(1000)
            print("{} final balance is {}".format(self.name,RaceCondition.account.get_balance()))



#test
# create the thread objects
t1= RaceCondition("Chetan")
t2=RaceCondition("Ashish")
t3=RaceCondition("Virendra")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()