from binascii import b2a_uu
from tkinter import *
main=Tk()
main.configure(bg="yellow")

L1=Label(main, text="Enter Your Name",font="Arial")
t1=Entry(main,width=20)
L2=Label(main, text="Enter Password",font="Arial")
t2=Entry(main,width=20,show="*")
b1=Button(main,text="Click Me",font="Arial",width=30)
text=Text(main)
text.grid(row=3,column=1)
#grid : arrange theelemnts in row and column
L1.grid(row=0,column=0)#1st row and 1st column
t1.grid(row=0,column=1)#1st row and 2nd column
L2.grid(row=1,column=0)#2nd row and 1st column
t2.grid(row=1,column=1)#2nd row and 2nd column
b1.grid(row=2,column=0,columnspan=2)

main.mainloop()