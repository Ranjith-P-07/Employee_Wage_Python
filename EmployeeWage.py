# Created by Ranjith P at 30-11-2020
import random


class Employee:

    def employeeAttendance(self):
        '''
        This is a Employee Attendence checking method
        :return:Present or Absent
        :rtype: str
        '''
        check = random.randint(1, 2)
        if check == 1:
            return "Present"
        else:
            return "Absent"


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")
    emp = Employee()
    print(emp.employeeAttendance())
