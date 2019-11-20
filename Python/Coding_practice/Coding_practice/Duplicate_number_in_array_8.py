

arr = [1, 2, 3, 4, 5, 1, 2, 5, 3]


# Finding dupliccate numbers
for i in range(len(arr)):
    for j in range(i):
        if arr[i] == arr[j]:
            print(arr[i], end=" ")


lst = []
# removing Duplicate element from list
for k in arr:
    if k not in lst:
        lst.append(k)
print(lst)


# Finding duplicate
