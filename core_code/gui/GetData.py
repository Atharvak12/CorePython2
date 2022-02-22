import tkinter
main = tkinter.Tk()
main.geometry("200x200")
#input varaible
v1=tkinter.StringVar()
def getData():
    data=v1.get()#get the value of inpout field
    tkinter.Label(main,text="Hello {}".format(data)).pack()
    
t1=tkinter.Entry(main,textvariable=v1)
t1.pack()
b1=tkinter.Button(main,text="Click me",command=getData)
b1.pack()
main.mainloop()
