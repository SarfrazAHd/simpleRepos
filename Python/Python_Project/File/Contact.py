from tkinter import  *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect("file.db")
curs = conn.cursor()


print("########################## Menu List ##########################")

print("Select Option from menu :")

print("1. Add Contact")
print("2. Delete Contact")
print("3. Update Contact")
print("4. All Contact")
print("5. Exit")


def viwe_all():
	print("########################## Contact List ##########################")

	sql = "SELECT * FROM  Contact"

	res=curs.execute(sql)
	row=res.fetchall()
	print("Name","        ","   Contact","         ","   Email")
	for i in row:
		id = i[0]
		Name = i[1]
		Gender = i[2]
		Address =i[3]
		Contact = i[4]
		Email = i[5]
		
		print(Name, "         ",Contact,  "       ",Email)


def Add_contact():
	print("########################## New Contact ##########################")
	name = input(" Enter Name : ")
	gender = input(" Enter Gender : ")
	address = input(" Enter Address : ")
	contact = input(" Enter Contact : ")
	email = input(" Enter Email   : ")
	sql = "INSERT INTO 'Contact'(Name, Address,Gender, Contact, Email) VALUES(?, ?, ?, ?, ?)"
	curs.execute(sql, (name, gender, address, contact, email,))
	conn.commit()
	print("Your data has been Saved Succesfully")




choice = input("Enter your choice: ")
if choice == '5':
	exit()


elif choice == '4':
	viwe_all()

elif choice == '1':
	Add_contact()





def Delete_contact():
	pass

def Update_contact():
	pass



	



