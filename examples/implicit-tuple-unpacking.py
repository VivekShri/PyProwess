# -*- coding: utf-8 -*-
"""
Created on 17-03-2019 at 02:52 PM

@author: Vivek
"""

# Function returning multiple values of different data types
def someFunction():
    name = 'Alice'
    ID = 'EMP001'
    salary = 10000
    return name, ID, salary

if __name__ == '__main__':
    # Multiple assignment
    x, y = 10, 20
    print('X:',x,'Y:',y)

    # Temporary tuple, pass-by-value assignment
    x, y = y, x
    print('X:', x, 'Y:', y)

    # String data type assignment
    x, y = 'OK'
    print('X:', x, 'Y:', y)

    # Multiple function return value assignment
    empName, empID, empSalary = someFunction()
    print('Name:', empName, ', ID:', empID, ', Salary:', empSalary)

    # Automatically unpacking elements of a list inside a loop
    list = [('Alice', 25), ('Bob', 30), ('Jake', 27), ('Barbara', 40)]
    for name, age in list:
        print(name, 'is aged', str(age))
