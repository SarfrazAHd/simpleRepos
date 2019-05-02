'''               ##this is the only for self-Practice:

#Linear search using While loop:
pos=-1
def search(lst,x):
    i=0
    while i<len(lst):
        if lst[i] == x:
            globals() ['pos']=i
            return True
        i=i+1
        
    return False

lst=[3,4,35,45,2,34,2,523,52,32,5,2,532]
x=int(input("enter your searching element: "))

if search(lst,x):
    print("Founded at",pos )

else:
    print("Not Founded") 




#Linear search using for loop:


position=-1
def search(a,b):
    
    for i in range(len(item)):
        if item[i]== y:
            globals()['position']=i
            return True
    return False


item=[54,45,754,3,3,436,346,7,54,6,55,33,434,4]
y=int(input("enter your searching element: "))


if search(item,y):
    print("founded at", position)

else:
    print("Not founded!") 




# Binary Search using for loop

pos=-1
def Bsrch(a,b):

    l=0
    u=len(lst)

    for i in range(u):
        mid= (l+u) // 2

        if lst[mid] == y:


            globals()['pos']=mid
            return True

        else:
            if lst[mid]< y:
                l=mid
            else:
                u=mid
    return False

lst=[-3, 0, 2, 9, 52, 62,80,90,100]
y=int(input("Enter searching element: "))



if Bsrch(lst,y):
    print("Found at :",pos)

else:
    print("Not Found:")






#Fibonacci series


def fib(a):
    a,b=0,1
    for i in range(n):
        print(a,end=",")
        a,b=b,a+b
    print()


n=int(input("enter the length of series: "))

fib(n)   


##Factorial Without Recursion:

def fact(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    print(x)
        

fact(10)  









##Factorial using Recursion:


def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

print(factorial(10))  




##Reverse of any String Using Loop:

def Reverse(strings):
    reversed_string =' '
    for i in strings:
        reversed_string=i+reversed_string

    print("Your Reversed String Is=>", reversed_string)

inpt=input("Enter any string: ")
Reverse(inpt)   


# Reverse of any String Using Slicing Method:

x=input("Enter any strings:")
print(x[::-1])










###Printing Some star Pattern:
#1

n=5
for i in range(n):
    for j in range(i+1):
        print("*" ,end=" ")

    print()

    


#2

m=5
for i in range(m):
    for j in range(m-i):
        print("*",end=' ')

    print()

#3

y=5
for i in range(1,y+1):
    for j in range(1,i+1):
        print(i,end=' ')

    print()  



#4

y=5
for i in range(1,y+1):
    for j in range(1,i+1):
        print(j,end=' ')

    print()
    










# Bubble Sort in Python !!



def Srt(a):
    
    for i in range(len(item)-1,0,-1):
        for j in range(i):
            if item[j]> item[j+1]:
                temp = item[j]
                item[j] = item[j+1]
                item[j+1] = temp




item = [56,43,34,676,85423,23235,575,42,9,64,7,10,-4]


Srt(item)
print("Your sorted Elements are:" ,item)     







###SelectionSort

def Srt(a):


    for i in range(len(itm)):
        minpos=i
        for j in range(i+1,len(itm)):
            if itm[j]<itm[minpos]:
                minpos=j

        itm[i],itm[minpos]=itm[minpos],itm[i]




itm=[9,2,52,62,0,-3]
Srt(itm)
print(itm)









#BubbleSort :



def Srt(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
a=[9,2,52,62,0,-3]
Srt(a)
print(a)



# Processing bar in python

import sys,time

for i in range(20):
    sys.stdout.write(' # ')
    sys.stdout.flush()
    time.sleep(0.1)

print (" Done!!")


'''









































































































































