n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print("*" ,end="")
    print()

n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*" ,end="")
    print()


n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i):
        print("*" ,end="")
    print()


n=int(input("Enter number of rows: "))
for i in range(n+1):
    for j in range(i+1):
        print(i ,end="")
    print()

n=int(input("Enter number of rows: "))
for i in range(n+1):
    for j in range(i+1):
        print(j ,end="")
    print()


#factorial of any number without recursion

n=int(input("Enter the number for factorial: "))
f=1
for i in range(1,n+1):
    f=f*i


x=f
print(x)


# Using recursion method

def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

print(fact(5))



def solveMeFirst(a,b):
    return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter seceond Number: "))
res = solveMeFirst(num1,num2)
print (res)



