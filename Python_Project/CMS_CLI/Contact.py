import sqlite3

conn = sqlite3.connect("file.db")
curs = conn.cursor()


def home():
    print("================ Menu List ================")

    print("Select Option from menu :")

    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. View All Contact")
    print("5. Exit")


def viwe_all():
    print("================ Contact List ================")

    sql = "SELECT * FROM  Contact"

    res = curs.execute(sql)
    row = res.fetchall()
    print("Id     Name    Gender    Address   Contact     Email", )
    for i in row:
        id = i[0]
        Name = i[1]
        Gender = i[2]
        Address = i[3]
        Contact = i[4]
        Email = i[5]

        print(id, "    ", Name, "  ", Gender, "  ", Address, "  ", Contact, "   ", Email)


def Add_contact():
    print("================ New Contact ================")
    name = input("  Enter Name : ")
    gender = input("  Enter Gender : ")
    address = input("  Enter Address : ")
    contact = input("  Enter Contact : ")
    email = input("  Enter Email   : ")

    if name == '' and gender == '' and address == '' and contact == '' and email == '':
        print("No data for save!")


    else:

        sql = "INSERT INTO 'Contact'(Name, Address,Gender, Contact, Email) VALUES(?, ?, ?, ?, ?)"
        curs.execute(sql, (name, gender, address, contact, email,))
        conn.commit()
        print("  Contact saved succesfully")


def delete_contact():
    print("================ Delete Contact ================")
    global name
    name = input("  Search name for delete: ")
    sql = "SELECT * FROM Contact WHERE Name  LIKE ?"
    res = curs.execute(sql, (name,))

    for i in res:
        id = i[0]
        name = i[1]
        gender = i[2]
        address = i[3]
        contact = i[4]
        email = i[5]
        print("================ Contact Detials ================")

        print("  Id : ", id)
        print("  Name : ", name)
        print("  Gender: ", gender)
        print("  Address is: ", address)
        print("  Contact : ", contact)
        print("  Email : ", email)

        confirmation = input("  Are you sure to delete(Y/N): ")

        def cnf_delete():
            sql = "DELETE FROM Contact Where Name LIKE?"

            curs.execute(sql, (name,))
            conn.commit()

            print("  Contact has been succesffully Deleted !!")

            back = input("  Delete another contact (Y/N): ")

            if back == 'Y' or back == 'YES' or back == 'yes' or back == 'y':
                delete_contact()

        if confirmation == 'y' or confirmation == 'Y' or confirmation == 'yes' or confirmation == 'YES':
            cnf_delete()



def Update_contact():
    print("================ Update Contact ================")
    name = input("  Search By name: ")
    sql2 = "SELECT * FROM Contact WHERE Name  LIKE ?"
    res2 = curs.execute(sql2, (name,))

    for i in res2:
        id = i[0]
        name = i[1]
        gender = i [2]
        address = i[3]
        contact = i[4]
        email = i[5]

        print("id is", id)

        print("Name is", name)
        names =input("New name: ")

        print("gender is", gender)
        gendes = input("New gender: ")

        print("Address is", address)
        addresss =input("New address: ")
        print("Contact is", contact)
        contacts = input("New contact: ")
        print("Email is", email)
        emails =input("New Email: ")

       
       
       
       
       


        sql3 = "UPDATE  Contact  set Name=?, Gender=?, Address=?, Contact=?, Email=? WHERE Name  LIKE ?"
        curs.execute(sql3, (names, gendes, addresss, contacts, emails, name))
        conn.commit()

        print("Data has been succesfully Updated")

while True:

    home()
    choice = input("  Enter your choice: ")

    if choice == '1':
        Add_contact()


    elif choice == '2':
        delete_contact()


    elif choice == '3':
        Update_contact()

    elif choice == '4':
        viwe_all()


    elif choice == '5':
        print("Application  closed! ")
        exit()

