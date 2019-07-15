
# Inheritance is an important concept of OOP
# A sub class can acquire all properties of it's super class or parent class
# But a super class can't acquire properties od it's subclass



class A:

    def function1(self):
        print("This is function 1")

    def function2(self):
        print("This is function 2")


class B:

    def function3(self):
        print("This is function 3 of class b ")

    def function4(self):
        print("This is function 4 of class B")


# Multiple inheritance  because it's acquiring feature of both class A and Class B
class C(B, A):
    def function5(self):
        print("This is function 5 of class b ")


a1 = A()
b1 = B()
c1 = C()
c1.function3()






