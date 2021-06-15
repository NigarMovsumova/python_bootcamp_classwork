# 1. Human classinin attributlarini ve 2 magic metodunu yazmaq
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('I eat')

    def breathe(self):
        print('I breathe')

    def __str__(self):
        return 'Human: name: {}, age: {} '.format(self.name, self.age)


class Employee(Human):

    def __init__(self, name, age, workplace, salary, vacation_days):
        super(Employee, self).__init__(name, age)
        self.workplace = workplace
        self.salary = salary
        self.vacation_days = vacation_days

    def work(self):
        print('I work')

    def __str__(self):
        return super(Employee, self).__str__() + \
               "workplace:{}, salary:{}, vacation_days:{}" \
                   .format(self.workplace, self.salary, self.vacation_days)


employee = Employee('Ali', 17, 'Google', 20000, 40)
print(employee)
