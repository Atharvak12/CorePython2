def hello():
    for i in range(1,16):
        print("hello {}".format(i))

def hi():
    for j in range(1,16):
        print("hi {}".format(j))
        
import threading

t1=threading.Thread(target=hello)
t2=threading.Thread(target=hi)

t1.start()
t2.start()
