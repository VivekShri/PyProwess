# -*- coding: utf-8 -*-
"""
Created on 17-03-2019 at 10:52 AM

@author: Vivek
"""

import time

def timeIt(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        print('Time:', endTime - startTime, 'seconds')

    return wrapper

@timeIt
def loadLargeFile(filename):
    print('Loading file:',filename)
    time.sleep(2) # Mocking long operation with a sleep call

@timeIt
def makeAPICall():
    print('Making an API call and waiting for the response...')
    time.sleep(1.5) # Mocking long operation with a sleep call

@timeIt
def generateSummaryReport():
    print('Generating summary report...')
    time.sleep(5) # Mocking long operation with a sleep call

if __name__ == '__main__':
    loadLargeFile('abc.txt')
    makeAPICall()
    generateSummaryReport()