from DATA.class_methods import Company

def search_employee(conn):
    cursor = conn.cursor()

    while True:
        employee_info = {}

        username = input("Enter employee name or 'exit' to quit: ").strip()

        if username.lower() == "exit":
            print("Returning to menu...")
            break

        cursor.execute("""
            SELECT com.created_at, com.department, sec.employee, sec.salary
            FROM company com
            JOIN sections sec
            ON com.id = sec.department_id
            WHERE sec.employee = ?
            ORDER BY com.created_at
        """, (username.upper(),))

        info = cursor.fetchall()

        if not info:
            print("Employee not found.")
            continue

        for row in info:
            date = row["created_at"]
            department = row["department"]

            if date not in employee_info:
                employee_info[date] = {}

            if department not in employee_info[date]:
                employee_info[date][department] = {}

            employee = row["employee"]
            salary = row["salary"]

            employee_info[date][department][employee] = salary

        return employee_info


def search_section(conn):
    cursor = conn.cursor()

    while True:
        department_info = {}

        user = input("Enter department name or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Returning to menu...")
            break

        cursor.execute(""" SELECT com.created_at, com.department, sec.employee, sec.salary
                   FROM company com JOIN sections sec ON com.id = sec.department_id
                   WHERE com.department = ? """, (user.upper(),))

        section = cursor.fetchall()

        if not section:
            print("Department not exist.")
            continue

        for row in section:
            date = row["created_at"]
            department = row["department"]
            employee = row["employee"]
            salary = row["salary"]

            if date not in department_info:
                department_info[date] = {}
            if department not in department_info[date]:
                department_info[date][department] = Company(department)   # if we want to use the add method ,
                                                                          # we store the main object on the equivalent key (department)
            department_info[date][department].add_employee(employee, salary)

        return department_info


def show_top_employees(conn):
    cursor = conn.cursor()

    while True:
        employees = {}

        try:
            user = input(
                "Enter number of employees to show based on highest salary or 'exit' to quit: "
            ).strip()

            if user.lower() == "exit":
                print("Returning to menu...")
                return None

            user_limit = int(user)

        except ValueError:
            print("Invalid input.")
            continue

        cursor.execute("""
            SELECT com.department, sec.employee, sec.salary
            FROM company com
            JOIN sections sec ON com.id = sec.department_id
            ORDER BY sec.salary DESC
            LIMIT ?
        """, (user_limit,))

        rows = cursor.fetchall()

        if not rows:
            print("No employees found.")
            continue

        for row in rows:
            department = row["department"]
            employee = row["employee"]
            salary = row["salary"]

            if department not in employees:  # if the department does not exist in the dictionary create a Company object for it
                employees[department] = Company(department)

            # if it already exists, the if statement is skipped so it will just add employee, salary to the existent department
            employees[department].add_employee(employee, salary)

        return employees
