
class student:




    # this init method work as a constructor to initialize variable
    def __init__(self, name, age, course, address):

        self.name = name
        self.age = age
        self.course = course
        self.address = address

    def features(self):
        print("Your name is", self.name, "age is ", self.age, "Your course is ", self.course, "And you address is",self.address)

stu = student("Sarfraz", 20, "B.Tech", "Gorakhpur")

stu.features()
