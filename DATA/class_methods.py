class Company():
    def __init__(self, department):
        self.department = department
        self.sections = {}

    def add_employee(self, employee, salary):
        self.sections[employee] = salary


    @classmethod
    def avg_tl_salaries_employees(cls, company):
        total_salaries = 0
        total_employees = 0
        if not company :
            return None, None, None

        for obj in company.values():
            for salary in obj.sections.values():
                total_salaries += salary
                total_employees += 1
        average = round((total_salaries / total_employees),2)  if total_employees > 0 else 0

        return average, total_employees, total_salaries

    @classmethod
    def avg_per_section(cls, company):
        section_averages = {}

        if not company :
            return section_averages

        for department,obj in company.items() :

            total_per_section = sum(obj.sections.values())
            employees = len(obj.sections)
            average = round((total_per_section / employees),2) if employees > 0 else 0

            section_averages[department] = average

        return section_averages

    @classmethod
    def top_low_employees(cls, company):
        top_salary = float("-inf")
        top_employee = ''
        top_employee_section = ''
        low_salary = float("inf")
        low_employee = ''
        low_employee_section = ''

        if not company :
            return None, None, None, None, None, None

        for department, obj in company.items():
            for employee , salary in obj.sections.items():

                if salary > top_salary:
                    top_salary = salary
                    top_employee = employee
                    top_employee_section = department

                if salary < low_salary:
                    low_salary = salary
                    low_employee = employee
                    low_employee_section = department

        return (top_salary, top_employee,top_employee_section,
                low_salary, low_employee,low_employee_section
        )

    @classmethod
    def top_low_employees_v2(cls, company):    # this fc equal the one before it, for learning purpose

        employees = []

        for department, obj in company.items():
            for employee, salary in obj.sections.items():
                employees.append((salary, employee, department))

        if not employees:
            return None, None, None, None, None, None

        top_salary, top_employee, top_section = max(employees)
        low_salary, low_employee, low_section = min(employees)

        return (
            top_salary, top_employee, top_section,
            low_salary, low_employee, low_section
        )
