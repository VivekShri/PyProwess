# -*- coding: utf-8 -*-
"""
Created on 17-03-2019 at 02:42 PM

@author: Vivek
"""

# The for-else loop to return the first even number or a '-1' if an even number is not found
def findEven(listOfNums):
    for number in listOfNums:
        if number % 2 == 0:
            return(number)
    else:
        return -1

if __name__ == '__main__':
    listOfEvenNums = [1, 7, 3, 4, 5]
    print('Return Value:',findEven(listOfEvenNums))

    listOfOddNums = [1, 1, 3, 5, 5]
    print('Return Value:',findEven(listOfOddNums))
