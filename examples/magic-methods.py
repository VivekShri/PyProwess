# -*- coding: utf-8 -*-
"""
Created on 17-03-2019 at 02:59 PM

@author: Vivek
"""

class Employee:
    # Constructor
    def __init__(self, name, ID, salary):
        self.empName = name
        self.empID = ID
        self.empSalary = salary

    # Defines behaviour when called using print() or str()
    def __str__(self):
        return 'Employee(' + self.empName + ',' + self.empID + ',' + str(self.empSalary) + ')'

    # Defines behaviour when called with repr()
    def __repr__(self):
        return '[' + self.empID + '] - ' + self.empName

    # Defines behaviour when called with '+' operator
    def __add__(self, secondObject):
        return (self.empSalary+secondObject.empSalary)

if __name__ == '__main__':
    objAlice = Employee('Alice','EMP001',10000)
    print(objAlice)
    print(repr(objAlice))

    print('')
    objBob = Employee('Bob', 'EMP002', 5000)
    print(objBob)
    print(repr(objBob))

    print('\nSum:',objAlice+objBob)
