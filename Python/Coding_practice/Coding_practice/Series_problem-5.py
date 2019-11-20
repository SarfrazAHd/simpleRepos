
# 1 1 2 3 4 9 8 27 16 81 32 ......

# odd terms are         1 2 4 8 16 32
# even terms are        1 3 9 27 81 343


n = int(input("Enter your terms: "))

a, b = 1, 1

for i in range(1, n+1):
    if (i%2!=0):
        if i == 1:
            a = 1
        else:
            a = a*2

    else:
        if i == 2:
            b = 1
        else:
            b = b*3


if (n%2!=0):
    print("{} term of the seris is {}".format(n, a))
else:
    print("{} term of the seris is {}".format(n, b))
