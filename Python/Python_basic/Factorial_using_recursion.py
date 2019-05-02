#Fiding Factorial
def factorial(x):
    a=1
    for i in range(1,x+1):
        a=a*i
        print(a)

factorial(10)


#Using recursion mehtod

def fact_rec(a):
    if a==0:
        return 1


    return a*fact_rec(a-1)

x=fact_rec(10)
print(x)
