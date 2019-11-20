array = [2, 34, 34, 5, 5, 10, 24, 150, 5, 34]

for i in range(len(array)):
    for j in range(i):
        if array[i] == array[j] > 1:  # Number repeating
            print(array[i], end=",")  # for more than one
