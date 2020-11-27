from inheritance.Person import Person


class Employee(Person):

    def make_money(self):
        print('I can make money')

    def count_income(self, salary):
        return salary


employee = Employee()
employee.make_money()
employee.breeze()
