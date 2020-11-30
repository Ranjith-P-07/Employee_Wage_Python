# Created by Ranjith P at 30-11-2020
import random


class Employee:
    check = random.randint(0, 1)

    def employee_attendance(self):
        '''
        This is a Employee Attendence checking method
        :return:Present or Absent
        :rtype: str
        '''
        if Employee.check == 1:
            return "Present"
        else:
            return "Absent"

    def emp_daily_wage(self):
        '''
        This is to Calculate Daily Wage Of Employee
        :return: salary
        :rtype: int
        '''
        if Employee.check == 1:
            emprateperhour = 20
            empworkinghour = 8
            salary = emprateperhour * empworkinghour
            return salary
        else:
            salary = 0
            return salary


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employee_attendance())
    print(emp.emp_daily_wage())
