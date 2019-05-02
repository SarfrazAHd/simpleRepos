pos=-1
def Search(item,x):

    i=0
    while i<len(item):
        if item[i] == x:
            globals()['pos']=i
            return True
        i=i+1

    return False

item=[2,3,43,5,343,543,543,643,6,434,3,6,64,5,756,8,769,8,5,756]

x=int(input("enter searching element: "))


if Search(item,x):
    print("Founed at" ,pos)
else:
    print("Not Founded!")
