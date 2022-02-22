from tkinter import *
main=Tk()
l1=Label(main,text="Top",fg="Green",bg="cyan")
l2=Label(main,text="Bottom",fg="Green",bg="cyan")
l3=Label(main,text="Left",fg="Green",bg="cyan")
l4=Label(main,text="Right",fg="Green",bg="cyan")

#set the elemnts on the window
l1.pack(side=TOP,padx=20,pady=20,ipady=40,ipadx=40)
l2.pack(side=BOTTOM)
l3.pack(side=LEFT,padx=20,pady=20)
l4.pack(side=RIGHT)

main.mainloop()