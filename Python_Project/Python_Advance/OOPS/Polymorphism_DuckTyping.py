
# Polymorphis = Poly (many) + Morph(Form)
# In OOPs when an object can hold more than one form that calll as polymorphism .


class Mycharm:
    def execute(self):
        print("Kindly smile you are in Mycharm section ")
        print("This is mycharm section ")


class IntelliJ:

    def execute(self):
        print("Kindly smile you are in IntelliJ section ")
        print("This is Intellij section ")

class Editor:

    def code(self, ide):
        ide.execute()


ide = Mycharm()
edi = Editor()

edi.code(IntelliJ())
