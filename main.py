from DATA.input_data import get_company
from DATA.class_methods import Company
from LOGIC.calculations import (
    below_above_company_avg,
    high_less_paid_department,
    top_low_per_department,
    department_above_avg
)
from DATA.SQL import create_connection, create_table, insert_into_table
from LOGIC.tools import search_employee, search_section, show_top_employees

def enter_and_analyze_company(conn):       # those analysis are based on data in memory not database

    company_data = get_company()
    if not company_data:
        print("No data entered.")
        return {}

    avg_salary, total_employees, total_salaries = Company.avg_tl_salaries_employees(company_data)

    print(f"Company average salary: {avg_salary} | Total employees: {total_employees} | Total salaries: {total_salaries}")

    section_averages = Company.avg_per_section(company_data)

    print("\nAverage salary per department:")
    for dep, avg in section_averages.items():
        print(f"  {dep}: {avg}")

    top_salary, top_employee, top_section, low_salary, low_employee, low_section = Company.top_low_employees(company_data)

    print(f"\nHighest paid employee: {top_employee} ({top_salary}) in {top_section}")
    print(f"Lowest paid employee: {low_employee} ({low_salary}) in {low_section}")


    below, above = below_above_company_avg(company_data)

    print(f"Employees below company avg: {below}")
    print(f"Employees above company avg: {above}")

    highest_dep, lowest_dep, high_avg, low_avg = high_less_paid_department(company_data)

    print(f"\nHighest avg department: {highest_dep} ({high_avg})")
    print(f"Lowest avg department: {lowest_dep} ({low_avg})")

    top_low_department = top_low_per_department(company_data)

    print("\nTop & lowest employees per department:")
    for dep, data in top_low_department.items():
        print(f"{dep} - Top: {data['top_employee']} | Low: {data['min_employee']}")

    section_above_avg, section_below_avg = department_above_avg(company_data)

    print(f"\nDepartments above company avg: {section_above_avg}")
    print(f"Departments below company avg: {section_below_avg}")

    # Ask user to save
    save_choice = input("\nDo you want to save this company data to the database? (y/n): ").strip().lower()

    if save_choice == "y":
        insert_into_table(conn, company_data)
        print("Company data saved to database successfully.")
    else:
        print("Data not saved. You can save later if needed.")

    return company_data


def main():
    conn = create_connection()
    create_table(conn)

    while True:
        print("\n===== COMPANY SYSTEM MENU by RAIJIN CODE =====")
        print("1. Add company, departments, and employees + analysis")
        print("2. Search employee by name")
        print("3. Search section by department")
        print("4. Show top employees by salary")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            enter_and_analyze_company(conn)

        elif choice == "2":
            result = search_employee(conn)
            if result:
                for date, dep_dict in result.items():
                    print(f"\nDate: {date}")
                    for dep, emp_dict in dep_dict.items():
                        print(f"Department: {dep}")
                        for emp, salary in emp_dict.items():
                            print(f"  Employee: {emp} | Salary: {salary}")

        elif choice == "3":

            result = search_section(conn)
            if result:
                for date, dep_dict in result.items():
                    print(f"\nDate: {date}")
                    for dep, obj in dep_dict.items():
                        print(f"Department: {dep}")
                        for emp, salary in obj.sections.items():
                            print(f"  Employee: {emp} | Salary: {salary}")

        elif choice == "4":

            top_employees = show_top_employees(conn)
            if top_employees:
                for dep, obj in top_employees.items():
                    print(f"\nDepartment: {dep}")
                    for emp, salary in obj.sections.items():
                        print(f"  Employee: {emp} | Salary: {salary}")

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main()