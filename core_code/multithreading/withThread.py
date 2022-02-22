# #create the target functions
# def hello():
#     for i in range(1,16):
#         print("Hello ",i)

# def hi():
#     for i in range(1,16):
#         print("Hi ",i)
# #2. import the threading module
# import threading
# #3. create a new thread objects
# t1=threading.Thread(target=hello)
# t2=threading.Thread(target=hi)
# #4. start the thread objects
# t1.start()
# t2.start()


#create the target functions
def hello(name):
    for i in range(1,51):
        print(name,"Hello ",i)

def hi(name):
    for i in range(1,51):
        print(name,"Hi ",i)
        
#2. import the threading module
import threading
#3. create a new thread objects
t1=threading.Thread(target=hello,args=("Ashish",),daemon=True)
t2=threading.Thread(target=hello,args=("Chetan",))
# t2=threading.Thread(target=hi,args=("Chetan",))
#4. start the thread objects
t1.start()
t2.start()