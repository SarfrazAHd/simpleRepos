x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))


def get_LCM(a, b, c):
    if a > b and c:
        greater = a
    elif b > c and a:
        greater = b
    else:
        greater = c

    while True:

        if (greater % a == 0 and greater % b == 0 and greater % c == 0):
            get_LCM = greater
            break
        greater += 1
    return get_LCM



print("LCM of these 3 numbers are: ", get_LCM(x, y,z))
