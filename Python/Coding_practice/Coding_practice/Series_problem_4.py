# series is
# 0 0 7 6 14 12 21 18 28 24 35 . . . . . . .

#odd term = 0 7 14 21 28 35                         is multiple of 7
#even term = 0 6 12 18 24 30                        is multiple of 6


n = int(input("Enter your term of the series: "))

a = 0
b = 0



for i in range(1, n+1):
    if (i%2!=0):
        if a == 1:
            a = 1
        else:
            a = a+7

    else:
        if b == 2:
            b = 1
        else:
            b = b + 6

if (n%2 == 0):
    print("{} term of the series  is {}".format(n, b-6))

else:
    print("{} term of the series  is {}".format(n, a-7))