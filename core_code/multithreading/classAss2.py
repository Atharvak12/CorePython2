from threading import Thread
import threading

class CalFactorial(Thread):
    def __init__(self,num,name):
        super().__init__()
        self.number = num#instance variable4
    
    def run(self):
        fact=1
        temp=self.number# create a local copy of the instance variable
        for i in range(1,temp+1):
            fact*=i #OR fact=fact*i
        print("{} Factorial {} is={}".format(threading.current_thread(),self.number,fact))


t1=CalFactorial(3,name="t1")
t2=CalFactorial(5,name="t2")

t1.start()
t2.start()
