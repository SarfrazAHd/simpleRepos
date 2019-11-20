itm = [12, 4, 5, 5, 23, 52, 2, 41, 1, 4, 8, 2, 0, 10]

y = 10
count = 0

for i in range(len(itm)):
    for j in range(i + 1, len(itm)):
        if itm[i] + itm[j] == y:
            print(itm[i])
            count += 1
print("total numbers are ", count)
