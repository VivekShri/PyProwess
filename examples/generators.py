# -*- coding: utf-8 -*-
"""
Created on 17-03-2019 at 03:03 PM

@author: Vivek
"""
import sys
import time

# Normal function
def getList(limit):
    listVal = list()
    for i in range(limit):
        listVal.append(i)

    return listVal

# Generator function
def genList(limit):
    for i in range(limit):
        yield i # This line also transfers the control back to the caller

    # A generator can have multiple 'yield' statements

if __name__ == '__main__':
    numLimit = 10000000

    # Creates the whole list BEFORE processing starts, even though elements are needed one-by-one
    print('\nWithout Generators:')
    startTime = time.time()
    numList = getList(numLimit)
    endTime = time.time()
    print(' - Time:', endTime - startTime, 'seconds')
    print(' - Size:', sys.getsizeof(numList))

    # The allocated size is low because the elements have not been used. Generators don't process till the element is called upon to be processed
    print('\nWith Generators:')
    startTime = time.time()
    numGenerator = genList(numLimit)
    endTime = time.time()
    print(' - Time:', endTime-startTime, 'seconds')
    print(' - Size:', sys.getsizeof(numGenerator))
