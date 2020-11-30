# Created by Ranjith P at 30-11-2020
import random


class Employee:
    part_time_emp_hr = 4
    full_time_emp_hr = 8
    emp_rate_per_hr = 20
    emp_hour = 0
    max_working_hour = 100
    max_working_days = 20
    daily_wage = []

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
        total_working_hours = 0
        total_working_days = 0
        working_hours = 0
        while total_working_hours <= Employee.max_working_hour and total_working_days <= Employee.max_working_days:
            total_working_days += 1
            self.employee_attendance()
            daily_wage = Employee.emp_rate_per_hr * Employee.emp_hour
            total_working_hours += Employee.emp_hour
            total_salary = total_salary + daily_wage
            working_hours = working_hours + Employee.emp_hour
            Employee.daily_wage.append(daily_wage)
            print(f"Employee Daily Wage is : {daily_wage}")
        print(f"Total Employee Working Hour is : {working_hours}")
        print(f"Total Wage for Month is : {total_salary}")


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employee_attendance())
    print(emp.calculate_daily_emp_wage())
    print(Employee.daily_wage)
