from cgitb import text
from tkinter import *
main=Tk()
main.title("My Frame")
main.geometry("200x200")
main.configure(bg="lime")

b1=Button(main,text="Button1")
b2=Button(main,text="Button2")
b3=Button(main,text="Button3")
b4=Button(main,text="Button4",command=main.quit)

b1.pack(side=LEFT,ipady=30,ipadx=30)
b2.pack(side=RIGHT,ipady=30,ipadx=30)
b3.pack(side=TOP,ipady=30,ipadx=30,pady=50)
b4.pack(side=BOTTOM,ipady=30,ipadx=30)

main.mainloop()