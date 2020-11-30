# Created by Ranjith P at 30-11-2020
import random


class Employee:
    part_time_emp_hr = 4
    full_time_emp_hr = 8
    emp_rate_per_hr = 20
    emp_hour = 0
    absent = 0

    def employee_attendance(self):
        '''
        This is a Employee Attendence checking method
        :return:Present or Absent
        :rtype:str
        '''
        check = random.randint(0, 2)
        if check == 1:
            Employee.emp_hour = 8
            return "Full Time Employee is Present"
        elif check == 2:
            Employee.emp_hour = 4
            return "Part Time Employee is Present"
        else:
            Employee.emp_hour = 0
            return "Absent"

    def calculate_daily_emp_wage(self):
        total_salary = 0
        for day in range(1,20):
            self.employee_attendance()
            daily_wage = Employee.emp_rate_per_hr * Employee.emp_hour
            total_salary = total_salary + daily_wage
            print(f"Employee Daily Wage is : {daily_wage}")
        return print(f"Total Wage for Month is : {total_salary}")


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employee_attendance())
    print(emp.calculate_daily_emp_wage())
