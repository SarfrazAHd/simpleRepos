from tkinter import *

import tkinter.ttk as ttk

root = Tk()

root.title("Python GUI Application ")

Label(root, text="Hierachical Treeview", font=('', 15, ''), bg='cadet blue').pack(side=TOP, fill=X)

tree = ttk.Treeview(root, columns=("Srudent Id", "Firstname", "Lastname", "BirthDate", "Programme", "Branch"),
                    selectmode="extended")

tree.heading('Srudent Id', text="Srudent Id", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('BirthDate', text="BirthDate", anchor=W)
tree.heading('Programme', text="Programme", anchor=W)
tree.heading('Branch', text="Branch", anchor=W)

tree.column('#0', stretch=NO, width=80)
tree.column('#1', stretch=NO, width=80)
tree.column('#2', stretch=NO, width=80)
tree.column('#3', stretch=NO, width=80)
tree.column('#4', stretch=NO, width=80)
tree.column('#5', stretch=NO, width=80)

tree.pack()
root.mainloop()
