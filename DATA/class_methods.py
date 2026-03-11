class Company():
    def __init__(self, department):
        self.department = department
        self.sections = {}

    def add_employee(self, employee, salary):
        self.sections[employee] = salary
