from DATA.class_methods import Company

def below_above_company_avg(company):
    below = {}
    above = {}
    if company :
        result = Company.avg_tl_salaries_employees(company)
        if result :
            avg_salary, total_employees, total_salaries = result
            for obj in company.values():
                for employee ,salary in obj.sections.items():

                   if avg_salary > salary:
                       below[employee] = salary
                   if avg_salary < salary:
                       above[employee] = salary

        return below, above

    return below, above

def high_less_paid_department(company):
    averages = Company.avg_per_section(company)
    if not averages:
        return averages

    highest = max(averages, key=averages.get)
    lowest  = min(averages, key=averages.get)

    return highest, lowest, averages[highest], averages[lowest]


def top_low_per_department(company):
    high_low_per_department = {}

    if not company:
        return high_low_per_department

    for department, obj in company.items():

        if not obj.sections:
            continue   # skip this department and go to the next one,it is for safety (department can be without employee)

        top_employee = max(obj.sections, key=obj.sections.get)
        min_employee = min(obj.sections, key=obj.sections.get)

        high_low_per_department[department] = {
            "top_employee": (top_employee, obj.sections[top_employee]),
            "min_employee": (min_employee, obj.sections[min_employee])
        }

    return high_low_per_department

def department_above_avg(company):

    result = Company.avg_tl_salaries_employees(company)
    department_averages= Company.avg_per_section(company)
    department_above_com_avg = {}
    department_below_com_avg = {}
    if not company:

        return department_above_com_avg, department_below_com_avg

    avg_salary, total_employees, total_salaries = result

    for department, averages in department_averages.items():

        if avg_salary < averages:
            department_above_com_avg[department] = averages

        if avg_salary > averages:
            department_below_com_avg[department] = averages

    return department_above_com_avg, department_below_com_avg
