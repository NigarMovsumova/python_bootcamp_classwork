class Employee:
    company_name = 'Azerconnect'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}: name={self.name} ' \
               f'salary={self.salary}'


class SalesManager:
    pass

employee = Employee('Jan', 2750)
employee_new = Employee('Silvester', 3500)
print(employee)
print(employee.company_name)
print(Employee.company_name)
Employee.company_name = 'Azercell'
print(Employee.company_name)
print(employee.company_name)
print(employee_new.company_name)
Employee.company_name = None
print(Employee.company_name)
print(employee.company_name)
print(employee_new.company_name)

