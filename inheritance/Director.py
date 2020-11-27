class Director:

    # overloading
    def count_income(self, salary, bonus, transport, rent):
        return salary + bonus + transport + rent

    # override
    def count_income(self, salary):
        return salary - 100


director = Director()
# print(director.count_income(100))
print(director.count_income(500, 100, 100, 100))
