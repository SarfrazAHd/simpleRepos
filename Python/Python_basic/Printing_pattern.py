#pattern 1
#using while loopa

a=1
while a<=5:
    print("*" ,end=" ")
    b=1
    while b<5:
        print("#" ,end=" ")
        b=b+1

    a=a+1
    print()

print("Good Bye!!")

#pattern 2 Using for loop


for i in range(5):
    for j in range(5):
        print("@" ,end=" ")

    print()

print("Good bye!!") 

#Pattern 3:
for i in range(4):
    for j in range(i+1):
        print("$" ,end=" ")

    print()
print("Good Bye!!")    

#Pattern 4
for i in range(5):
    for j in range(5-i):
        print("#",end=" ")
    print()

print("Good bye!!")


