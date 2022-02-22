def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i#1*2*3*4*5
    print(fact,"\n")

import threading
t1=threading.Thread(target=factorial,args=(4,),name="T1")
t2=threading.Thread(target=factorial,args=(5,),name="T2")
t3=threading.Thread(target=factorial,args=(6,))
t4=threading.Thread(target=factorial,args=(7,))

t1.start()
t2.start()
t3.start()
t4.start()