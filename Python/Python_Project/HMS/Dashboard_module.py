# Hospital management system with  python and sqlite3


from tkinter import *
import tkinter.messagebox
import sqlite3

# connecting database

conn = sqlite3.connect("C:/Users/Nizam/PycharmProjects/SimpleRepos/Python/Python_Project/HMS/Hospital_mgmt_db.db")
curs = conn.cursor()

lists = []

root = Tk()
root.title("Hospital Appointment")

title = Label(root, text="XYZ Hospital Appointment", font=('times new roman', 35, 'bold'), fg="steelblue")
title.place(x=20, y=10)

# patient name
patient = Label(root, text="Patient Name  ", font=('arial', 16, 'bold'), fg="steelblue")
patient.place(x=20, y=100)

patient_ent = Entry(root, font=('airal', 12, ''), width=30)
patient_ent.place(x=250, y=100)

gen = Label(root, text="Gender", font=('arial', 16, 'bold'), fg = "steelblue")
gen.place(x=20, y=140)

gen_ent = Entry(root, font=('arial', 12, ''), width=30)
gen_ent.place(x=250, y=140)

Age = Label(root, text="Age", font=('arial', 16, 'bold'), fg = "steelblue")
Age.place(x=20, y=180)

Age_ent = Entry(root, font=('arial', 12, ''), width=30)
Age_ent.place(x=250, y=180)

loc = Label(root, text="Address", font=('arial', 16, 'bold'), fg = "steelblue")
loc.place(x=20, y=220)

Loc_ent = Entry(root, font=('arial', 12, ''), width=30)
Loc_ent.place(x=250, y=220)

time = Label(root, text="Appointment Time", font=('arial', 16, 'bold'), fg="steelblue")
time.place(x=20, y=260)

time_ent = Entry(root, font=('freesans', 12, ''), width=30)
time_ent.place(x=250, y=260)

sql2 = "SELECT Name  FROM Appointment "

sql2exec = curs.execute(sql2)

for i in sql2exec:
    name = i[0]
    lists.append(name)

final_name = len(lists)

box = Text(root, width=35, height=15, font=('times new roman', 13, 'italic'), fg="black")
box.place(x=549, y=100)

box.insert(END, "\n")
box.insert(END, "\n")
box.insert(END, "\n")

box.insert(END, "Total  Appointment till now is : " + str(final_name))

log = Label(root, text="Logs", font=('times new roman', 25, 'bold'), fg="steelblue", bg="white")
log.place(x=555, y=102)


def add_appoinment():
    val1 = patient_ent.get()
    val2 = gen_ent.get()
    val3 = Age_ent.get()
    val4 = Loc_ent.get()
    val5 = time_ent.get()

    if val1 == "" or val2 == "" or val3 == "" or val4 == "" or val5 == "":
        tkinter.messagebox.showinfo("Warning", "Please enter all details")

    else:
        sql = "INSERT INTO 'Appointment'(Name, Gender, Age, Address, Appoint_time) VALUES(?, ?, ?, ?, ?)"
        curs.execute(sql, (val1, val2, val3, val4, val5))
        conn.commit()
        tkinter.messagebox.showinfo("Congrats", "You succesfully booked you appointent")
        box.insert(END, "\n")
        box.insert(END, str(val1) + " your appointment has been fixed at " + str(val5))


btn = Button(root, font=('arial', 10, 'bold'), text="Add appoinment", width=20, fg='white', height=2, bg="steelblue", command=add_appoinment)
btn.place(x=300, y=300)

root.geometry("870x690+0+0")
root.resizable(False, False)

root.mainloop()
