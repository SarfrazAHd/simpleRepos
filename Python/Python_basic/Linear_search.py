lst=[34,43,5,6,4,5,45,435,45,5,765,6,6576]

x=int(input("Enter searching element:"))


def fun(a,b):

    pos=1
    for i in range(len(lst)):
        if lst[i] == x:

            globals() ['pos']=i
            return True
    return False


if fun(lst,x):
    print("Founded at",pos)
else:
    print("Not Founded!")
    






