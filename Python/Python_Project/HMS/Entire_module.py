from tkinter import *
import tkinter.messagebox
import sqlite3


import time

root = Tk()
root.title("Home Page")

# connecting database

conn = sqlite3.connect("Hospital_mgmt_db.db")
curs = conn.cursor()

sql = "SELECT * FROM Appointment"

res = curs.execute(sql)

for i in res:
    name = i[0]
    gender = i[1]
    age = i[2]
    address = i[3]
    time = i[4]

patient = []

number = []

title = Label(root, text="Welcome to XYZ Hospital", font=('times new roman', 30, 'bold'), fg="steelblue")
title.place(x=170, y=15)

appointment = Label(root, text="Appointment System", font=('times new roman', 25, 'bold'), fg="steelblue")
appointment.place(x=240, y=70)

usr=Label(root, text="Enter username", font=('times new roman', 16, 'bold'), fg="black")
usr.place(x=326, y=150)
usr_ent=Entry(root, font=('times new roman', 13, ''),width=28, relief=FLAT)
usr_ent.place(x=285, y=180)


Pass=Label(root, text="Enter Password", font=('times new roman', 16, 'bold'), fg="black")
Pass.place(x=326, y=235)
Pass_ent=Entry(root, font=('times new roman', 13, ''), show='*',width=28, relief=FLAT)
Pass_ent.place(x=285, y=265)


def hide():
	global hide 
	hide=root.destroy()


lists=[]

def seceond_window():
	hide
	root = Tk()
	root.title("Hospital Appointment")



	title = Label(root, text="XYZ Hospital Appointment", font=('times new roman', 35, 'bold'), fg="steelblue")
	title.place(x=20, y=10)

	# patient name
	patient = Label(root, text="Patient Name  ", font=('times new roman', 16, 'bold'), fg="steelblue")
	patient.place(x=20, y=100)

	patient_ent = Entry(root, font=('times new roman', 11, ''), width=35)
	patient_ent.place(x=220, y=100)

	gen = Label(root, text="Gender", font=('times new roman', 16, 'bold'), fg = "steelblue")
	gen.place(x=20, y=140)

	gen_ent = Entry(root, font=('times new roman', 11, ''), width=35)
	gen_ent.place(x=220, y=140)

	Age = Label(root, text="Age", font=('times new roman', 16, 'bold'), fg = "steelblue")
	Age.place(x=20, y=180)

	Age_ent = Entry(root, font=('times new roman', 11, ''), width=35)
	Age_ent.place(x=220, y=180)

	loc = Label(root, text="Address", font=('times new roman', 16, 'bold'), fg = "steelblue")
	loc.place(x=20, y=220)

	Loc_ent = Entry(root, font=('times new roman', 11, ''), width=35)
	Loc_ent.place(x=220, y=220)

	time = Label(root, text="Appointment Time", font=('times new roman', 16, 'bold'), fg="steelblue")
	time.place(x=20, y=260)

	time_ent = Entry(root, font=('times new roman', 11, ''), width=35)
	time_ent.place(x=220, y=260)

	sql2 = "SELECT Name  FROM Appointment "

	sql2exec = curs.execute(sql2)

	for i in sql2exec:
	    name = i[0]
	    lists.append(name)

	final_name = len(lists)

	box = Text(root, width=35, height=15, font=('times new roman', 13, 'italic'), fg="black")
	box.place(x=520, y=100)

	box.insert(END, "Total  Appointment till now is : " + str(final_name))
	log = Label(root, text="Logs", font=('times new roman', 17, 'bold'), fg="steelblue")
	log.place(x=532, y=65)


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


	btn = Button(root, font=('arial', 9, 'bold'), text="Add appoinment", width=14, fg='white', height=1, bg="steelblue", command=add_appoinment)
	btn.place(x=300, y=300)

	def hide2():
		root.destroy()

	def modify():

		hide2()
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

		        details = Label(root, text="your current detaisl are .....", font=('times new roman', 12), fg="grey")
		        details.place(x=105, y=164)

		        Name = Label(root, text="Name  ", font=('times new roman', 16, 'bold'), fg="steelblue")
		        Name.place(x=105, y=190)

		        Name_ent = Entry(root, font=('airal', 12, ''), width=30)
		        Name_ent.place(x=300, y=185)
		        Name_ent.insert(END, name)

		        gen = Label(root, text="Gender", font=('times new roman', 16, 'bold'), fg="steelblue")
		        gen.place(x=105, y=225)

		        gen_ent = Entry(root, font=('arial', 12, ''), width=30)
		        gen_ent.place(x=300, y=225)
		        gen_ent.insert(END, gender)

		        Ages = Label(root, text="Age", font=('times new roman', 16, 'bold'), fg="steelblue")
		        Ages.place(x=105, y=268)

		        Age_ent = Entry(root, font=('arial', 12, ''), width=30)
		        Age_ent.place(x=300, y=268)
		        Age_ent.insert(END, Age)

		        loc = Label(root, text="Address", font=('times new roman', 16, 'bold'), fg="steelblue")
		        loc.place(x=105, y=315)

		        Loc_ent = Entry(root, font=('arial', 12, ''), width=30)
		        Loc_ent.place(x=300, y=315)
		        Loc_ent.insert(END, Address)

		        time = Label(root, text="Appointment Time", font=('times new roman', 16, 'bold'), fg="steelblue")
		        time.place(x=105, y=357)

		        time_ent = Entry(root, font=('freesans', 12, ''), width=30)
		        time_ent.place(x=300, y=357)
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

		    updbtn = Button(root, font=('times new roman', 10, 'bold'), text="Update", width=11, height=1, fg='white', bg="steelblue", command=update)
		    updbtn.place(x=300, y=410)

		    delbtn = Button(root, font=('times new roman', 10, 'bold'), text="Delete", width=11, height=1, fg='white', bg="red", command=delete)
		    delbtn.place(x=420, y=410)

		
		def update_Back():

			root.destroy()
			seceond_window()

		backbtn=Button(root, font=('times new roman', 11,'bold'), text="Back", width=11, height=1, fg='white', bg="brown", command=update_Back)
		backbtn.place(x=620, y=10)


		btn = Button(root, font=('times new roman', 10, 'bold'), text="Search", width=11, fg='white', height=1, bg="orange",command=update_appointment)
		btn.place(x=280, y=130)

		root.geometry("840x500+0+0")
		root.resizable(False, False)

		root.mainloop()

	update = Button(root, font=('arial', 9, 'bold'), text="Update appoinment", width=17, fg='white', height=1, bg="orange", command=modify)
	update.place(x=290, y=350)

	root.geometry("870x500+0+0")
	root.resizable(False, False)
	root.mainloop()

def login():
	if usr_ent.get()=="abhishek" and Pass_ent.get()=="pragati":
		seceond_window()

	else:
		tkinter.messagebox.showinfo("Error", "Enter correct credentials")
		usr_ent.delete(0, END)
		Pass_ent.delete(0, END)


patient_btn = Button(root, font=('times new roman', 12, 'bold'), text="Login to DashBoard", width=17, bg='brown', height=1,fg="white",command=login)
patient_btn.place(x=330, y=330)


root.geometry("840x500+0+0")
root.resizable(False, False)
root.mainloop()
