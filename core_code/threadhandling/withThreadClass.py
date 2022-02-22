from threading import Thread
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.__name = name
    
    def run(self):
        for i in range(1,16):
            print("{} Hello {}".format(i,self.__name,))


#create thread object
t1=MyThread("Ajay")
t2=MyThread("Vijay")
t1.setName("Ajay")
print(t1.getName())
print(t2.getName())
t1.start()
t1.join(1)#join after me
t2.start()