

class galgotia:



    class_variable = "Galgotia University"


    def __init__(self,m1,m2, m3):

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method
    def instance_method(self):
        print(self.m1, self.m2, self.m3)

    # in instance method  we have 2 things 1 >: Accesor(fetching Value) 2 >: Mutator(Updating value)
    def accesor(self):                                         # this will access the value of instance variable
        print(self.m1)

    def mutator(self, value):
        self.m1 = value                                         #  this will modify the value of our instance varible



    # class Method
    @classmethod
    def class_method(cls):
        return cls.class_variable



    # Statice method
    @ staticmethod
    def static_method():
        print("This is static method section")




g1 = galgotia(14, 45, 145)
g1.instance_method()
g1.accesor()
print(g1.class_method())

g1.static_method()


