from tkinter import *
import  tkinter.messagebox
import sqlite3
import pyttsx3

import time


root=Tk()
root.title("Home Page")


# connecting database

conn=sqlite3.connect("C:/Users/Nizam/Database/Hospital_mgmt_db.db")
curs=conn.cursor()


sql="SELECT * FROM Appointment"

res=curs.execute(sql)


for i in res:
    name=i[0]
    gender=i[1]
    age=i[2]
    address=i[3]
    time=i[4]


patient=[]

number=[]


title=Label(root,text="Welcome to XYZ Hospital",font=('times new roman',35,'bold'),fg="steelblue")
title.place(x=170,y=30)

appointment=Label(root,text="Appointment System",font=('times new roman',30,'bold'),fg="steelblue")
appointment.place(x=240,y=110)




patient_btn=Button(root,font=('times new roman',12,'bold'),text="New Patient",width=15,bg='green',height=2,fg="white")
patient_btn.place(x=330,y=410)
























root.geometry("870x690+0+0")
root.resizable(False,False)


root.mainloop()