




pos = - 1
def Binary_search(x,y):
    l = 0
    u = len(itm)

    for i in range(u):
        mid = (l+u) // 2

        if itm[mid] == y:
            globals()['pos'] = mid
            return True
        else:
            if y > itm[mid]:
                l = mid

            else:
                u = mid

    return False
    

itm = [-1, 0, 1, 2, 3, 4, 5, 6, 23, 66, 76, 534]

Searching_element = int(input("Enter your searching elements: "))

if Binary_search(itm, Searching_element):
    print("Element {} Found at {} index ".format(Searching_element, pos))
else:
    print("Element does not exist in list")


# Complexity

# Worst-case: 0 (log n)
# Best-case : O(1)

# Space Case complexity: O(1)







