
class a :
    def fun1(self):
        print("funcion 1")

    def fun2(self):
        print("funcion 2")


class b(a):
    def fun3(self):
        print("funcion 3")

    def fun4(self):
        print("funcion 4")

A = b()

A.fun4()