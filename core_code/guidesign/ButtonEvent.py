from tkinter import *

window=Tk()
window.geometry("300x300")
def left_click():
    Label(window,text="Left click").pack()

def right_click():
    Label(window,text="Right click").pack()
    

Button(window,text="Left Click",command=left_click).pack()
Button(window,text="RIght Click",command=right_click).pack()

# window.bind("<Button-1>",left_click)
# window.bind("<Button-3>",right_click)

window.mainloop()
