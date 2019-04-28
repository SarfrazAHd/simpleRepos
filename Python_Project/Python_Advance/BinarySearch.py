# Linear Search Using For loop

pos = -1


def Search(a, b):
    for i in range(len(list)):

        if list[i] == x:
            globals()['pos'] = i
            return True
    return False


list = [1, 24, 435, 436, 67, 65, 786, 867]
x = int(input("Enter searching Element:"))

if Search(list, x):
    print("Found at", pos)

else:
    print("Not Found!")

# Binary Search

position = -1


def BSearch(a, b):
    l = 0
    u = len(itm)

    for i in range(u):
        mid = (l + u) // 2
        if itm[mid] == y:
            globals()['position'] = mid
            return True
        else:
            if itm[mid] < y:
                l = mid

            else:
                u = mid

    return False


itm = [2, 3, 4, 20, 23, 46, 57, 60, 65]  # In Binary Search All element Should be in sorted List.
y = int(input("Enter searching Element:"))

if BSearch(itm, y):
    print("Founded at", position)
else:
    print("Not Founded!")
