
# PolyMorphism, When an object in oops consist it;s multiple 
# form Called Polymorphism 

#  Method Overloading
# same method but with differents-with different  parameters

class A:

    def sum(self, m1=None, m2=None, m3=None):

        if m3!=None and m2!=None and m1!=None:
            s = m1+m2+m3
            return s

        elif m1!=None and m2!=None:
            return m1+m2
        else:
            return m1


a = A()
print(a.sum(10, 20, 30))



#  Method Overriding
# same method  with same parameters but with different class

class A:

    def show(self):
        print("In class A ")

class B(A):

    def show(self):
        print("In class B ")


a = B()
a.show()


