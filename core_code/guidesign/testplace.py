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
l1=Label(main,text="Enter Your Name",font="Arial",fg="Red",bg="Green")
l2=Label(main,text="Enter password",font="Arial",fg="Red",bg="Green")
#single line input
t1=Entry(main,width=50,font="Times")
t2=Entry(main,width=50,font="Times",show="*")

#button input
b1=Button(main,text="Sign In",font="Arial 30",fg="Red",bg="Green")
#geometry maagement
l1.place(x=50,y=50)
t1.place(x=300,y=50)
l2.place(x=50,y=100)
t2.place(x=300,y=100)
b1.place(x=75,y=150)#2nd row 1st col
main.mainloop()