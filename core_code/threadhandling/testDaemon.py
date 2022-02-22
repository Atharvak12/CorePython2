def hello(name):
    for i in range(1,16):
        print("{} Hello {}".format( i,name))


from threading import Thread

import threading
main=threading.main_thread()
# print(main)
# t1=Thread(target=hello,args=("Atharv",),daemon=True)
t1=Thread(target=hello,args=("Atharv",))
t2=Thread(target=hello,args=("Ajay",))
t3=Thread(target=hello,args=("Vijay",))

# print(t1)
# print(t2)
# print(t3)
# main.join()
t2.start()
t3.start()
t1.start()

# print(threading.enumerate())
# print(threading.get_ident())
# print(threading.current_thread())
# print("Active thread",threading.active_count())
