from threading import Thread
#. create a class 
#2. Inherit The Thread class

class MyThread(Thread):
    def __init__(self,n,daemon=False):
        super().__init__()
        self.name=n
    
    #3. override the run method
    def run(self):
        for i in range(1,51):
            print("{} Hello {}".format(i,self.name))

#4. create the thread class object
t1= MyThread("Ashish",daemon=True)
t2= MyThread("Virendra")
t3= MyThread("Chetan")
import threading
print("------------------------------------")
print("Active Thraeds:",threading.active_count())
print("All Threads:",threading.enumerate())
#5. start the thread
t1.start()
t2.start()
t3.start()
print("------------------------------------")
print("Active Thraeds:",threading.active_count())
print("All Threads:",threading.enumerate())


