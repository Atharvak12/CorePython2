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
l2=Label(main,text="Enter Password",font="Arial 30")
#single line input
t1=Entry(main,width=50,font="Times")
t2=Entry(main,show="*")

#button input
b1=Button(main,text="Sign In")
#geometry maagement
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
main.mainloop()