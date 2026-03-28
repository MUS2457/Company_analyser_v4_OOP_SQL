Company Analyzer v4

A Python CLI application that stores and analyzes company employee data using SQLite.
The program allows you to record departments, employees, and salaries, then perform different analyses on the stored data.

This project focuses on database usage, modular Python structure, and data analysis with SQL queries.

Features
Add company data (departments, employees, salaries)
Store data in an SQLite database
Search employees in the database
Analyze company salary data
Show top employees by salary
Find departments with higher or lower salary averages
Perform structured analysis using SQL queries

Example SQL Query Used

Example: counting employees by salary level

SELECT department, AVG(salary)
FROM sections
GROUP BY department

This query calculates the average salary per department.

What I Practiced in This Project
Working with SQLite databases
Writing JOIN queries
Using GROUP BY for analysis
Designing modular Python applications
Separating data layer and logic layer
Building CLI-based data analysis tools
