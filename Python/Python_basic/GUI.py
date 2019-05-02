from tkinter import *
import math
root=Tk()
root.title("Welcome to GUI")
Entry(root).pack()
label=Label(root, text="Welcome to Python GUI", bg="red",fg="white",height=10,width=15)
label.pack()
Button(root,text="Radio button",fg="green").pack()
root.mainloop()
