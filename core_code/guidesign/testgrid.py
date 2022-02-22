# import tkinter
# import tkinter as tk
from tkinter import *

main=Tk()
#set the title for the main window
main.title("My Window")
#initial window size
main.geometry("500x500")
main.configure(bg="cyan")
#label: uneditable text
l1=Label(main,text="Enter Your Name",font="Arial 30",fg="Red",bg="Green")
l2=Label(main,text="Enter password",font="Arial 30",fg="Red",bg="Green")
#single line input
t1=Entry(main,width=50,font="Times")
t2=Entry(main,width=50,font="Times",show="*")

#button input
b1=Button(main,text="Sign In",font="Arial 30",fg="Red",bg="Green",width=60)
#geometry maagement
l1.grid(row=0,column=0)#1st row 1st col
t1.grid(row=0,column=1)#1st row 2nd col
l2.grid(row=1,column=0)#2nd row 1st col
t2.grid(row=1,column=1)#2nd row 2nd col
b1.grid(row=2,column=0,columnspan=2)#2nd row 1st col
main.mainloop()