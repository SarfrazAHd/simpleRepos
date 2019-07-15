n = int(input("Enter range for getting prime number"))

for i in range(1, n):
    if n > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break

        else:
            print(i)
