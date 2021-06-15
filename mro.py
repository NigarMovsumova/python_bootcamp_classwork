class Human:
    def test(self):
        print('I am a Human')


class Employee:
    def test(self):
        print('I am an employee')


class Teacher(Human, Employee):
    pass
    # def test(self):
    #     print('I am a teacher')


teacher = Teacher()
teacher.test()
print(Teacher.mro())
print(teacher)

# __str__


