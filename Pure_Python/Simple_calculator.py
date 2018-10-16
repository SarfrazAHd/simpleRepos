def add(x, y):
    return x + y


def Sub(x, y):
    return x - y


def Mul(x, y):
    return x * y


def div(x, y):
    return x / y


print("Enter your choice for Operation :")
print("1- for addition")
print("2- for Subtraction")
print("3- for Multiplication")
print("4- for Division")

choice = int(input("Enter your chiice :"))

if choice == 1:
    num1 = int(input("enter first number "))
    num2 = int(input("enter seceond number "))
    z = add(num1, num2)
    print("Your result is => " + str(z))

elif choice == 2:
    num1 = int(input("enter first number "))
    num2 = int(input("enter seceond number "))
    z = Sub(num1, num2)
    print("Your result is => " + str(z))

elif choice == 3:
    num1 = int(input("enter first number "))
    num2 = int(input("enter seceond number "))
    z = Mul(num1, num2)
    print("Your result is => " + str(z))

elif choice == 4:
    num1 = int(input("enter first number "))
    num2 = int(input("enter seceond number "))
    z = div(num1, num2)
    print("Your result is => " + str(z))

else:
    print("you have entered out of the choice !!")

