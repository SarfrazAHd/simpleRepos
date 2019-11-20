n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))


def get_HCF(x, y, z):
    if x > y and y > z :
        diff = x -(y-z)

    else:
        if y > z:
            diff = y - z
        else:
            diff = z - y


    while True:
        if x % diff == 0 and y % diff == 0 and z % diff == 0:
            get_HCF = diff
            break
        diff -= 1
    return get_HCF


print("HCF of these 3 numbers are ", get_HCF(n1, n2, n3))






