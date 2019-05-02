



class student:

    def __init__(self, m1, m2):

        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        return student(m1, m2)


    def __str__(self):
        return self.m1, self.m2

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False


s1 = student(50, 20)
s2 = student(20, 40)

s3 = s2 + s1

print(s1.__str__())

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")