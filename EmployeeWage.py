# Created by Ranjith P at 30-11-2020
import random


class Employee:
    check = random.randint(0, 2)
    emp_rate_per_hour = 20

    def employee_attendance(self):
        '''
        This is a Employee Attendence checking method
        :return:Present or Absent
        :rtype: str
        '''
        if Employee.check == 1:
            return "Full Time Employee is Present"
        elif Employee.check == 2:
            return "Part Time Employee is Present"
        else:
            return "Absent"

    def emp_daily_wage(self):
        '''
        This is to Calculate Daily Wage Of Employee
        :return: salary
        :rtype: int
        '''
        if Employee.check == 1:
            empworkinghour = 8
            salary = Employee.emp_rate_per_hour * empworkinghour
            return salary
        elif Employee.check == 2:
            empworkinghour = 4
            salary = Employee.emp_rate_per_hour * empworkinghour
            return salary
        else:
            salary = 0
            return salary


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employee_attendance())
    print(emp.emp_daily_wage())
