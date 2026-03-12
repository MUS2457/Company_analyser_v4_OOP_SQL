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

