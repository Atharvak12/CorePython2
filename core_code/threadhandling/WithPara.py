def hello(name):
    for i in range(1,16):
        print("{} hello {}".format(i,name))

def hi(name):
    for j in range(1,16):
        print("{} hi {}".format(j,name))
        
import threading

t1=threading.Thread(target=hello,args=("Ajay",))
t2=threading.Thread(target=hi,args=("Ashish",))

t1.start()
t2.start()
