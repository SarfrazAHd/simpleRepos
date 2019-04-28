
class student:


    class_variable=5

    def name(self):
        print("This is name section of student class")

        instance_variable = 6
        print(type(instance_variable), instance_variable)


stu = student()
stu.name()


student.name(student)




