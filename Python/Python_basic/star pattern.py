def add(x,y):
    return x+y

def subs(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
print("********************************************")
print("Select the operation that u want to perfrom :")
print("Enter 1 for Addition : ")
print("Enter 2 for Substraction : ")
print("Enter 3 for Multiplication : ")
print("Enter 4 for Division : ")

choice=int(input("Enter your choice : "))



if choice>4:
    print("You have entered out of range:")
if choice==1:

    j=int(input("enter the first numebr : "))
    k=int(input("enter the seceond numebr : "))

    x=add(j,k)
    print("Your result is => " +str(x))
   
elif choice==2:
    j=int(input("enter the first numebr : "))
    k=int(input("enter the seceond numebr : "))

    y=subs(j,k)
    print("Your result is => " +str(y))
    
elif choice==3:
    j=int(input("enter the first numebr : "))
    k=int(input("enter the seceond numebr : "))

    z=mul(j,k)
    print("Your result is => " +str(z))
elif choice==4:

    j=int(input("enter the first numebr : "))
    k=int(input("enter the seceond numebr : "))

    k=div(j,k)
    print("Your result is => " +str(k))
                 

print("Thanks For using Python IDLE ")
print("********************************************")

        
       
  




  

