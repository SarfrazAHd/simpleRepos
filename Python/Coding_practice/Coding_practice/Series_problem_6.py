# Series is 0 0 2 1 4 2 6 3 8 4 10 5 12 6 ...


# odd terms: 0 2 4 6 8 10 ..
# even terms : 0 1 2 4 5 6


n = int(input("Enter your terms: "))

a = 0
b = 0

for i in range(1, n+1):
    if (i%2!=0):
        if i == 1:
            a = 0
        else:
            a = a+2
    else:
        if i == 2:
            b = 0
        else:
            b = b+1


if (n%2!=0):
    print("{} term of the series is {}".format(n, a))
else:
    print("{} term of the series is {}".format(n, b))

