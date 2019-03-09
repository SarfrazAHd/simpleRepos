from tkinter import *
import sqlite3
import tkinter.messagebox

root = Tk()
root.title("Student Database Management Project")
root.config(bg="cadet blue")
root.geometry("1350x750+0+0")

con = sqlite3.connect("C:/Users/Nizam/Database/Student_database.db")
curs = con.cursor()


# Entire screen as a Frame
MainFrame = Frame(root, bg="cadet blue")
MainFrame.grid()



# Creating Frame size for title
TitleFrame = Frame(MainFrame, padx=50, pady=8, bd=2, bg="Ghost White", relief=RIDGE)
TitleFrame.pack(side=TOP)



# Student Heading Label  Frame
title = Label(TitleFrame, text="Student Database Management System", font=('arial', 35, 'bold'), width=43,
              bg="Ghost White", fg="brown", bd=2, relief=RIDGE)
title.pack(side=RIGHT)



# Student Label  Frame
DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, bg="cadet blue", padx=20, pady=30, relief=RIDGE)
DataFrame.pack(side=TOP)

DataFrameLeft = LabelFrame(DataFrame, width=900, height=500, padx=20, pady=20, relief=RIDGE, font=('arial', 20, 'bold'),
                           text="Student Information", bg="Ghost White")
DataFrameLeft.pack(side=LEFT)

DataFrameRight = LabelFrame(DataFrame, width=400, height=500, padx=10, pady=2, relief=RIDGE, font=('arial', 20, 'bold'),
                            text="Student Detabase", bg="Ghost White")
DataFrameRight.pack(side=RIGHT)


# Label and their Entry
Student_id = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Student Id ", padx=4, pady=6,
                   bg="Ghost White")
Student_id.grid(row=0, column=0, sticky=W)

Student_id_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_id_entry.grid(row=0, column=1)



Student_name = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Student Name ", padx=4, pady=6,
                     bg="Ghost White")
Student_name.grid(row=1, column=0, sticky=W)

Student_name_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_name_entry.grid(row=1, column=1)



Student_last_name = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Last Name ", padx=4, pady=6,
                          bg="Ghost White")
Student_last_name.grid(row=2, column=0, sticky=W)


Student_last_name_entry = Entry(DataFrameLeft, font=('arial', 14, ''), width=39)
Student_last_name_entry.grid(row=2, column=1)




Student_birth = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Date of Birth ", padx=4, pady=6,
                      bg="Ghost White")
Student_birth.grid(row=3, column=0, sticky=W)

Student_birth_entry = Entry(DataFrameLeft, font=('arial', 14, ''), width=39)
Student_birth_entry.grid(row=3, column=1)




Student_programme = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Programme", padx=4, pady=6,
                          bg="Ghost White")
Student_programme.grid(row=4, column=0, sticky=W)

Student_programme_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_programme_entry.grid(row=4, column=1)





Student_branch = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Branch", padx=4, pady=6,
                       bg="Ghost White")
Student_branch.grid(row=5, column=0, sticky=W)
Student_branch_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_branch_entry.grid(row=5, column=1)




Student_address = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Address", padx=4, pady=6,
                        bg="Ghost White")
Student_address.grid(row=6, column=0, sticky=W)
Student_address_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_address_entry.grid(row=6, column=1)




Student_email = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Email", padx=4, pady=6,
                      bg="Ghost White")
Student_email.grid(row=7, column=0, sticky=W)
Student_email_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_email_entry.grid(row=7, column=1)




Student_phone = Label(DataFrameLeft, font=('times new roman', 16, 'bold'), text="Phone Number", padx=4, pady=6,
                      bg="Ghost White")
Student_phone.grid(row=8, column=0, sticky=W)
Student_phone_entry = Entry(DataFrameLeft,  font=('arial', 14, ''), width=39)
Student_phone_entry.grid(row=8, column=1)




scrollbar = Scrollbar(DataFrameRight)
scrollbar.grid(row=0, column=4, sticky="ns")

list_box = Listbox(DataFrameRight, width=50, height=16, yscrollcommand=scrollbar.set,
                   font=('times new roman', 15, 'bold'))
list_box.grid(row=0, column=1, sticky="ns")
scrollbar.config(command=list_box.yview)


def add_new():
    id = Student_id_entry.get()
    Firstname = Student_name_entry.get()
    lastname = Student_last_name_entry.get()
    birth = Student_birth_entry.get()
    programme = Student_programme_entry.get()
    branch = Student_branch_entry.get()
    address = Student_address_entry.get()
    email = Student_email_entry.get()
    phone = Student_phone_entry.get()

    if id == "" or Firstname == "" or lastname == "" or birth == "" or programme == "" or branch == "" or address == "" or email == "" or phone == "":
        tkinter.messagebox.showinfo("Warning", "Enter details to add new student!")

    else:
        sql = "INSERT into 'Student_db'(SID, F_name, L_name, Birth_date, Programme, Branch, Address, Email,Contact ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

        curs.execute(sql, (id, Firstname, lastname, birth, programme, branch, address, email, phone))
        con.commit()
        tkinter.messagebox.showinfo("Succesfull", "Your data has been recorded")


btnFrame = Frame(MainFrame, width=70, height=30, padx=10, pady=10)
btnFrame.pack(side=BOTTOM)

btn1 = Button(btnFrame, text="Add New", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=add_new)
btn1.grid(row=0, column=1)


def display():
    list_box.delete(0, END)
    ress = con.execute("SELECT  * FROM Student_Db")
    rows = ress.fetchall()
    con.commit()
    for j in rows:
        list_box.insert(END, j)


btn2 = Button(btnFrame, text="Display", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=display)
btn2.grid(row=0, column=2)


def clear():
    if Student_id_entry.get() == "" and Student_name_entry.get() == "" and Student_last_name_entry.get() == "" and Student_birth_entry.get() == "" and Student_programme_entry.get() == "" and Student_branch_entry.get() == "" and Student_address_entry.get() == "" and Student_email_entry.get() == "" and Student_phone_entry.get() == "":
        tkinter.messagebox.showinfo("Clear", "No date for remove")

    else:
        Student_id_entry.delete(0, END)
        Student_name_entry.delete(0, END)
        Student_last_name_entry.delete(0, END)
        Student_birth_entry.delete(0, END)
        Student_programme_entry.delete(0, END)
        Student_branch_entry.delete(0, END)
        Student_address_entry.delete(0, END)
        Student_email_entry.delete(0, END)
        Student_phone_entry.delete(0, END)


# list_box.delete(0, END)

btn3 = Button(btnFrame, text="Clear", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=clear)
btn3.grid(row=0, column=3)


def delete():
    id = Student_id_entry.get()
    Firstname = Student_name_entry.get()
    lastname = Student_last_name_entry.get()
    birth = Student_birth_entry.get()
    programme = Student_programme_entry.get()
    branch = Student_branch_entry.get()
    address = Student_address_entry.get()
    email = Student_email_entry.get()
    phone = Student_phone_entry.get()

    if id == "" or Firstname == "" or lastname == "" or birth == "" or programme == "" or branch == "" or address == "" or email == "" or phone == "":
        tkinter.messagebox.showinfo("Warning!", "No data for Deletion")
    else:
        deletion = tkinter.messagebox.askyesno("Delete", "Are you sure you want to delete ?")

        if deletion > 0:

            sql = "DELETE FROM Student_db WHERE F_name LIKE?"
            curs.execute(sql, (Student_name_entry.get(),))
            con.commit()

            Student_id_entry.delete(0, END)
            Student_name_entry.delete(0, END)
            Student_last_name_entry.delete(0, END)
            Student_birth_entry.delete(0, END)
            Student_programme_entry.delete(0, END)
            Student_branch_entry.delete(0, END)
            Student_address_entry.delete(0, END)
            Student_email_entry.delete(0, END)
            Student_phone_entry.delete(0, END)

            tkinter.messagebox.showinfo("Delete", "Data has been Deleted")


btn4 = Button(btnFrame, text="Delete ", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=delete)
btn4.grid(row=0, column=4)


def search():

    if Student_id_entry.get() == "":
        tkinter.messagebox.showinfo("Search", "Enter Student id for search ")

    else:
        sql = "SELECT * FROM Student_db WHERE SID  LIKE ?"
        res = curs.execute(sql, ( Student_id_entry.get(),))
        Student_name_entry.delete(0, END)

        for i in res:
            id = i[0]
            Firstname = i[1]
            lastname = i[2]
            birth = i[3]
            programme = i[4]
            branch = i[5]
            address = i[6]
            email = i[7]
            phone = i[8]


        Student_id_entry.delete(0, END)
        Student_id_entry.insert(0, id)

        Student_name_entry.delete(0, END)
        Student_name_entry.insert(0, Firstname)

        Student_last_name_entry.delete(0, END)
        Student_last_name_entry.insert(0, lastname)

        Student_birth_entry.delete(0, END)
        Student_birth_entry.insert(0, birth)

        Student_programme_entry.delete(0, END)
        Student_programme_entry.insert(0, programme)

        Student_branch_entry.delete(0, END)
        Student_branch_entry.insert(0, branch)

        Student_address_entry.delete(0, END)
        Student_address_entry.insert(0, address)

        Student_email_entry.delete(0, END)
        Student_email_entry.insert(0, email)

        Student_phone_entry.delete(0, END)
        Student_phone_entry.insert(0, phone)






btn5 = Button(btnFrame, text="Search", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=search)
btn5.grid(row=0, column=5)


def update():
    id = Student_id_entry.get()
    Firstname = Student_name_entry.get()
    lastname = Student_last_name_entry.get()
    birth = Student_birth_entry.get()
    programme = Student_programme_entry.get()
    branch = Student_branch_entry.get()
    address = Student_address_entry.get()
    email = Student_email_entry.get()
    phone = Student_phone_entry.get()

    if id == "" or Firstname == "" or lastname == "" or birth == "" or programme == "" or branch == "" or address == "" or email == "" or phone == "":

        tkinter.messagebox.showinfo("Update", "No data for Update")

    else:
        sql = "UPDATE  Student_db SET SID=?, F_name=?, L_name=?, Birth_date=?, Programme=?, Branch=?, Address=?, Email=?, Contact=?  WHERE F_Name Like?"
        curs.execute(sql, (id, Firstname, lastname, birth, programme, branch, address, email, phone, Firstname))
        con.commit()
        tkinter.messagebox.showinfo("Updation", "Congrats! Data has been updated")




btn6 = Button(btnFrame, text="Update", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=update)
btn6.grid(row=0, column=6)


def exit():
    quit = tkinter.messagebox.askyesno("Student Database", "Do you want to Exit ?")
    if quit > 0:
        root.destroy()


btn7 = Button(btnFrame, text="Exit ", font=('times new roman', 16, 'bold'), padx=10, pady=5, width=10, relief=RIDGE,
              command=exit)
btn7.grid(row=0, column=7)

res = con.execute("SELECT  * FROM Student_Db")
row = res.fetchall()
con.commit()


index = 0
for i in row:
    x = i[1]
    index = index + 1
    list_box.insert(index, x)




menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
submenus = Menu(menubar, tearoff=0)
submenuss = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New file")
submenu.add_command(label="Open file")
submenu.add_command(label="Save file")

menubar.add_cascade(label="Edit", menu=submenus)
submenus.add_command(label="Cut")
submenus.add_command(label="Copy")
submenus.add_command(label="Paste")

menubar.add_cascade(label="Help", menu=submenuss)
submenuss.add_command(label="Help-Section")

root.mainloop()
