from inheritance.Person import Person


class Student(Person):

    def learn(self):
        print("I am learning a lot a day")


student = Student()
student.learn()
student.breeze()
