# Created by Ranjith P at 30-11-2020
import random


class Employee:
    part_time_emp_hr = 4
    full_time_emp_hr = 8
    emp_rate_per_hr = 20
    absent = 0
    check = random.randint(0, 2)

    def employee_attendance(self):
        '''
        This is a Employee Attendence checking method
        :return:Present or Absent
        :rtype:str
        '''
        if Employee.check == 1:
            return "Full Time Employee is Present"
        elif Employee.check == 2:
            return "Part Time Employee is Present"
        else:
            return "Absent"

    def getemp_working_hr(self):
        '''
        This method is Used to get Employee Working Hours
        :return: Employee Working Hour
        :rtype: int
        '''
        workHour = {0: Employee.absent, 1: Employee.full_time_emp_hr, 2: Employee.part_time_emp_hr}
        if Employee.check == 1:
            return workHour.get(1)
        elif Employee.check == 2:
            return workHour.get(2)
        else:
            return workHour.get(0)

    def calculate_daily_emp_wage(self, empHr):
        '''
        This method is to calculate Daily Employee Wage
        :param empHr: Employee Working Hour
        :type empHr: int
        :return: Daily Wage of Employees
        :rtype: int
        '''
        return Employee.emp_rate_per_hr * empHr


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employee_attendance())
    print(emp.calculate_daily_emp_wage(emp.getemp_working_hr()))