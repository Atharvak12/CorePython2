from binascii import b2a_uu
from tkinter import *
main=Tk()
main.configure(bg="#ffaa33")

L1=Label(main, text="Enter Your Name",font="Arial")
t1=Entry(main)
L2=Label(main, text="Enter Password",font="Arial")
t2=Entry(main,width=20,show="#")
b1=Button(main,text="Click Me",font="Arial")
L1.place(x=50,y=50)
t1.place(x=180,y=50)
L2.place(x=50,y=100)
t2.place(x=180,y=100)
b1.place(x=120,y=150)
main.mainloop()