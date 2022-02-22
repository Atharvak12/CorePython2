from tkinter import *

window=Tk()
n1=IntVar()
n2=IntVar()
n3=IntVar()

def add():
    a=n1.get()
    b=n2.get()
    c=a+b
    n3.set(c)
def clear():
    n1.set("")
    n2.set("")
    n3.set("")

t1=Entry(window,textvariable=n1,font="Arial")
l1=Label(window,text="+",font="Arial")
t2=Entry(window,textvariable=n2,font="Arial")
t3=Entry(window,textvariable=n3,font="Arial")
b1=Button(window,text="Add",command=add,font="Arial")
b2=Button(window,text="Clear",command=clear,font="Arial")
b3=Button(window,text="Close",command=window.quit,font="Arial")
l2=Label(window,text="=",font="Arial")

t1.grid(row=0,column=0)
l1.grid(row=0,column=1)
t2.grid(row=0,column=2)
l2.grid(row=0,column=3)
t3.grid(row=0,column=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

window.mainloop()
