from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()

root.maxsize(1400, 800)

root.title("Python-Notepad")
root.iconbitmap(r'icon.ico')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_area = Text(root, font=('Times new roman', 15, ''), height=400, width=400, yscrollcommand=scrollbar.set)
text_area.pack(fill=BOTH)
scrollbar.config(command=text_area.yview)


def open():
    global file

    file = filedialog.askopenfile(title="Select file to open ", filetypes=(("Text", "*.txt"), ("All files", "*.*")))

    if file != None:

        text_area.delete(1.0, END)

        for i in file:
            text_area.insert(END, i)

    

    root.title(" - Notepad" )


def new():
    text_area.delete(1.0, END)
    root.title("Untitled New file - Notepad")


def cut():
    text_area.event_generate(("<<Cut>>"))


def copy():
    text_area.event_generate(("<<Copy>>"))


def paste():
    text_area.event_generate(("<<Paste>>"))


def save():
    global file

    if file == None:


        save_file = filedialog.asksaveasfile(initialfile="Untitled.txt",  defaultextension="*.txt", filetypes=(("Text", "*.txt"), ("All files", "*.*")))

        if file == "":
            file = None
        else:
            f= open(file, 'w')

            f.write(text_area.get(1.0, END))
            f.close()

    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()





menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)
subMenus = Menu(menubar, tearoff=0)
subMenuss = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=subMenu)
menubar.add_cascade(label="Edit", menu=subMenus)
menubar.add_cascade(label="Help", menu=subMenuss)

subMenu.add_command(label="New File", command=new)
subMenu.add_command(label="Open File", command=open)
subMenu.add_command(label="Save file", command=save)



subMenu.add_command(label="Exit", command=root.quit)

subMenus.add_command(label="Cut", command=cut)
subMenus.add_command(label="Copy", command=copy)
subMenus.add_command(label="Paste", command=paste)

root.mainloop()
