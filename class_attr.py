class Employee:
    company_name = 'Azerconnect'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return '{}: name={} salary={}'.format(
            self.__class__.__name__, self.name, self.salary)


class SalesManager(Employee):
    base_salary = 350.00

    def __init__(self, name, sales_amount):
        self.name = name
        self.salary = sales_amount * 0.05 + SalesManager.base_salary


employee = SalesManager('Jan', 500)
employee_new = SalesManager('Silvester', 500)
print(employee)

employee = Employee('Jan', 2750)
employee_new = Employee('Silvester', 3500)
print(employee)

sales_manager = SalesManager('Arnold', 100000)
print(sales_manager)

# print(employee.company_name)
# print(Employee.company_name)
# Employee.company_name = 'Azercell'
# print(Employee.company_name)
# print(employee.company_name)
# print(employee_new.company_name)
# Employee.company_name = None
# print(Employee.company_name)
# print(employee.company_name)
# print(employee_new.company_name)
