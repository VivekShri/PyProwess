# -*- coding: utf-8 -*-
"""
Created on 01-04-2019 at 11:56 AM

@author: Vivek
"""

# Python imports
from functools import wraps
import unittest
import json

# Project modules imports
from api import API

# Defines
def disableAPICall(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        flagValue = self.objAPI.enableAPICall
        self.objAPI.enableAPICall = False
        print('Disabling API calls...')
        retVal = func(self, *args, **kwargs)
        print('Re-enabling API calls...')
        self.objAPI.enableAPICall = flagValue
        return retVal
    return wrapper

def disableStdout(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        stdOut = self.objAPI.enableStdout
        self.objAPI.enableStdout = False
        print('Disabling class STDOUTs...')
        retVal = func(self, *args, **kwargs)
        print('Re-enabling class STDOUTs...')
        self.objAPI.enableStdout = stdOut
        return retVal
    return wrapper


class Test_API(unittest.TestCase):
    def setUp(self):
        print('\n--------------------------------')
        self.objAPI = API()

    @disableAPICall
    @disableStdout
    def testConfig_getRandom(self):
        print('Testing config: getRandom')
        self.objAPI.getRandom()
        self.assertEqual(self.objAPI.apiURL, 'https://api.publicapis.org/random')
        self.assertDictEqual(self.objAPI.apiPayload, {'auth':'null'})

    @disableAPICall
    @disableStdout
    def testConfig_getAllCategories(self):
        print('Testing config: getAllCategories')
        self.objAPI.getAllCategories()
        self.assertEqual(self.objAPI.apiURL, 'https://api.publicapis.org/categories')

    @disableAPICall
    @disableStdout
    def testConfig_getEntry(self):
        print('Testing config with category: Business')
        self.objAPI.getEntry('business')
        self.assertEqual(self.objAPI.apiURL, 'https://api.publicapis.org/entries')
        self.assertDictEqual(self.objAPI.apiPayload, {'category':'business', 'https':True})

    def testResponse_getAllCategories(self):
        print('Testing response: getAllCategories')
        categories = self.objAPI.getAllCategories()
        print(' - Validating number of categories returned = 46')
        self.assertEqual(len(categories),46)

    @disableStdout
    def testResponse_getEntry_Business(self):
        print('Testing response for category: Business')
        self.objAPI.getEntry('business')
        responseJSON = json.loads(self.objAPI.response.text)
        print(' - Asserting keys in response JSON...')
        self.assertIn('count', responseJSON.keys())
        self.assertIn('entries', responseJSON.keys())

if __name__ == '__main__':
    unittest.main()