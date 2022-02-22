# import tkinter
# main=tkinter.Tk()
# main.geometry("400x400")
# main.title("Button Click Event")
# def hello():
#     tkinter.Label(main, text="Hello World",font="Arial").pack()

# b=tkinter.Button(main, text="Click me", command=hello)
# b.pack()
# main.mainloop()



import tkinter
main=tkinter.Tk()
main.geometry("400x400")
main.title("Button Click Event")
def hello(event):
    tkinter.Label(main, text="Hello World",font="Arial").pack()

b=tkinter.Button(main, text="Click me")
b.pack()
main.bind("<Button>",hello)
main.mainloop()