#Binary Search Using For loop

pos = -1
def Srch(a,b):

    l=0
    u=len(lst)


    for i in range(u):
        mid = (l+u) // 2

        if lst[mid] == y:
            globals() ['pos'] = mid
            return True 
        else:
            if lst[mid] < y:
                l = mid
            else:
                u = mid


    return False

lst = [2,4,6,7,8,10,11,23,30,35,40]
y =  int(input("Enter searchine element: "))

if Srch(lst,y):
    print("item founded at",pos)

else:
    print("item not founded!")
