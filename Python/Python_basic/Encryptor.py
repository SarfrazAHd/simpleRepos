



alphabet="abcdefghijklmnopqrstuvwxyz"

key=5

newmessage = ''
mystring = input("Enter your string for encryption: ")


for i  in mystring:
    if i in alphabet:

        position=alphabet.find(i)

        newposition=(position + int(key)) % 26

        newcharacter= alphabet[newposition]

        newmessage+=newcharacter

    else:
        newmessage+=newcharacter

print("Your encrypted message is: ",newmessage)
        

        

