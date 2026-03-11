from DATA.class_methods import Company

def get_department():
    while True:
        department = input("Enter department, 'done' to finish or 'quit' to quit ").strip()

        if any(char.isdigit() for char in department) or department == '':
            print("Invalid department, please try again.")
            continue
        elif department in ('done', 'quit'):
            return department.lower()

        return department.upper()


def get_employee(department):
    while True:
        employee = input(f"Enter employee from {department} and 'done' to finish  ").strip()

        if any(char.isdigit() for char in employee) or employee == '':
            print("Invalid employee, please try again.")
            continue
        elif employee == 'done':
            return employee.lower()

        return employee.upper()

def get_salary(department, employee):
    while True:
        try :
            salary = float(input(f"Enter salary of {employee} from {department}."))
            if salary < 0:
                print("Invalid salary, please try again.")
                continue
            return salary

        except ValueError:
            print("Invalid salary, please try again.")
            continue

def get_company():
    company = {}
    while True:
        department = get_department()

        if department == 'quit':
            print("Quitting... ")
            break
        elif department == 'done':
            break

        section = Company(department)

        while True:
            employee = get_employee(department)

            if employee == 'done':
                break

            salary = get_salary(department, employee)

            section.add_employee(employee, salary)

        company[department] = section

    return company