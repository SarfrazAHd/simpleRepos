# Hospital management system with  python and sqlite3
# this is update modeule in Python and  tkinter


from tkinter import *
import tkinter.messagebox
import sqlite3

# connecting database

conn = sqlite3.connect("C:/Users/Nizam/Database/Hospital_mgmt_db.db")
curs = conn.cursor()

root = Tk()
root.title("Update Appointment")

title = Label(root, text="Update Appointmenets", font=('times new roman', 35, 'bold'), fg="steelblue")
title.place(x=75, y=10)

patient = Label(root, text="Patient Name  ", font=('times new roman', 16, 'bold'), fg="steelblue")
patient.place(x=105, y=100)

patient_ent = Entry(root, font=('airal', 12, ''), width=30)
patient_ent.place(x=280, y=100)


def update_appointment():
    x = patient_ent.get()

    if x == "":
        tkinter.messagebox.showinfo("Warning ", "Kindly Enter patient Name")

    else:
        sql = "SELECT * FROM Appointment WHERE Name LIKE ?"

        res = curs.execute(sql, (x,))

        for i in res:
            name = i[0]
            gender = i[1]
            Age = i[2]
            Address = i[3]
            Appoint_time = i[4]

        # print("your age is "+ str(Age))

        details = Label(root, text="your current detaisl are .....", font=('arial', 11, 'italic'), fg="red")
        details.place(x=105, y=170)

        Name = Label(root, text="Name  ", font=('arial', 16, 'bold'), fg="steelblue")
        Name.place(x=105, y=210)

        Name_ent = Entry(root, font=('airal', 12, ''), width=30)
        Name_ent.place(x=300, y=200)
        Name_ent.insert(END, name)

        gen = Label(root, text="Gender", font=('arial', 16, 'bold'), fg="steelblue")
        gen.place(x=105, y=260)

        gen_ent = Entry(root, font=('arial', 12, ''), width=30)
        gen_ent.place(x=300, y=260)
        gen_ent.insert(END, gender)

        Ages = Label(root, text="Age", font=('arial', 16, 'bold'), fg="steelblue")
        Ages.place(x=105, y=320)

        Age_ent = Entry(root, font=('arial', 12, ''), width=30)
        Age_ent.place(x=300, y=320)
        Age_ent.insert(END, Age)

        loc = Label(root, text="Address", font=('arial', 16, 'bold'), fg="steelblue")
        loc.place(x=105, y=380)

        Loc_ent = Entry(root, font=('arial', 12, ''), width=30)
        Loc_ent.place(x=300, y=380)
        Loc_ent.insert(END, Address)

        time = Label(root, text="Appointment Time", font=('arial', 16, 'bold'), fg="steelblue")
        time.place(x=105, y=450)

        time_ent = Entry(root, font=('freesans', 12, ''), width=30)
        time_ent.place(x=300, y=450)
        time_ent.insert(END, Appoint_time)

    def update():
        val1 = Name_ent.get()
        val2 = gen_ent.get()
        val3 = Age_ent.get()
        val4 = Loc_ent.get()
        val5 = time_ent.get()

        query = "UPDATE  Appointment SET Name=?, Gender=?, Age=?, Address=?, Appoint_time=?  WHERE Name Like?"
        curs.execute(query, (val1, val2, val3, val4, val5, patient_ent.get()))
        conn.commit()

        tkinter.messagebox.showinfo("Update", "Updated Succesfully")

    def delete():

        query2 = "DELETE FROM  Appointment  WHERE Name Like?"
        curs.execute(query2, (patient_ent.get(),))
        conn.commit()

        tkinter.messagebox.showinfo("Delete", "Deleted Succesfully")

        Name_ent.destroy()
        gen_ent.destroy()
        Age_ent.destroy()
        Loc_ent.destroy()
        time_ent.destroy()

    updbtn = Button(root, font=('times new roman', 13, 'bold'), text="Update", width=7, height=1, fg='white', bg="steelblue", command=update)
    updbtn.place(x=300, y=515)

    delbtn = Button(root, font=('times new roman', 13, 'bold'), text="Delete", width=7, height=1, fg='white', bg="red", command=delete)
    delbtn.place(x=420, y=515)


btn = Button(root, font=('times new roman', 11, 'bold'), text="Search", width=7, fg='white', height=1, bg="steelblue",
             command=update_appointment)
btn.place(x=280, y=140)

root.geometry("870x690+0+0")
root.resizable(False, False)

root.mainloop()
