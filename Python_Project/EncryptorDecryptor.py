from tkinter import *
import random




root = Tk()
root.title("EncryptorDecryptor")
root.iconbitmap(r'C:/Users/Nizam/Downloads/lock.ico')       # give the location of your current *.ico image for title icon 

# width x height + x_offset + y_offset:
root.geometry("630x350+35+35")

root.iconbitmap()


l1=Label(root,font=('arial',15,'bold'),text="Enter your message : ",fg="black").grid(row=1,column=2)
l2=Label(root,font=('arial',15,'bold'),text="Encrypted message : ",fg="black").grid(row=5,column=2)
l3=Label(root,font=('arial',15,'bold'),text="Decrypt your message : ",fg="black").grid(row=9,column=2)
l4=Label(root,font=('arial',15,'bold'),text="Decrypted message: ",fg="black").grid(row=13,column=2)





v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()


e1=Entry(root,textvariable=v1,font=('aial',17,'bold'),bg='powder blue',fg="orange",bd=8).grid(row=1,column=6)
e2=Entry(root,textvariable=v2,font=('aial',17,'bold'),bg='powder blue',fg="orange",bd=8).grid(row=5,column=6)
e3=Entry(root,textvariable=v3,font=('aial',17,'bold'),bg='powder blue',fg="orange",bd=8).grid(row=9,column=6)
e4=Entry(root,textvariable=v4,font=('aial',17,'bold'),bg='powder blue',fg="orange",bd=8).grid(row=13,column=6)



alphabet = "abcdefghijklmnopqrstuvwxyz"
key=15


def encrypt():
    newmessage = ''
    mystring = v1.get()
    for character in mystring:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position + int(key))% 26
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    v2.set(newmessage)

    return


def decrypt():
    newmessage = ''
    mystring = v3.get()
    for character in mystring:
        if character in alphabet:
            position = alphabet.find(character)
            newposition = (position - int(key))% 26
            newcharacter = alphabet[newposition]
            newmessage += newcharacter
        else:
            newmessage += character
    v4.set(newmessage)

    return
5



b1=Button(root,font=('arial',10,'bold'),text="Encrypt",bd=8,bg="blue",fg="white",command=encrypt).grid(row=4,column=6)
b2=Button(root,font=('arial',10,'bold'),text="Decrypt",bd=8,bg="blue",fg="white",command=decrypt).grid(row=11,column=6)
Close_button=Button(root,padx=4,font=('arial',10,'bold'),text="CLOSE",fg="white",bg="blue",bd=8,command=root.quit).grid(row=17,column=6)


root.mainloop()
