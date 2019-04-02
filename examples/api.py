# -*- coding: utf-8 -*-
"""
Created on 22-03-2019 at 10:02 PM

@author: Vivek

NOTE: For the purpose of demo, I am using various public APIs from the Github repository: https://github.com/davemachado/public-api, powered by Digital Ocean
      The service was still in beta at the time of my usage, and if you are using the code at a later time, there may be some issues.
      The demo is only for explaining the usage of requests module must only be used for learning the basics. In a proper project, other additional measures might be needed to make sure
      that the APIs are used/deployed properly and safely.
"""

import requests
import json

URL_BASE = 'https://api.publicapis.org/'
URL_GET_CATEGORY = 'entries'
URL_GET_RANDOM = 'random'
URL_GET_ALL_CATEGORIES = 'categories'

class API:
    def __init__(self):
        print('Setting up API...')

        # Control parameters
        self.enableAPICall = True
        self.enableStdout = True

        # API parameters
        self.apiURL = None
        self.apiHeader = None
        self.apiPayload = None
        self.response = None


    def getEntry(self,categoryName):
        if self.enableStdout:
            print('\nFetching category:',categoryName)
        self.apiURL = URL_BASE + URL_GET_CATEGORY
        self.apiPayload = {'category':categoryName, 'https':True}

        if self.enableAPICall is True:
            self.response = requests.get(url=self.apiURL,params=self.apiPayload)
            responseJSON = json.loads(self.response.text)
            for key, value in responseJSON.items():
                if self.enableStdout:
                    print(' -', key, '=', value)


    def getRandom(self):
        if self.enableStdout:
            print('\nFetching random category...')
        self.apiURL = URL_BASE + URL_GET_RANDOM
        self.apiPayload = {'auth':'null'}

        if self.enableStdout:
            print('URL:',self.apiURL)
            print('Query params:',self.apiPayload)

        if self.enableAPICall is True:
            if self.enableStdout:
                print('API call is enabled')
            self.response = requests.get(url=self.apiURL,params=self.apiPayload)
            responseJSON = json.loads(self.response.text)
            for key, value in responseJSON.items():
                if self.enableStdout:
                    print(' -', key, '=', value)
        else:
            if self.enableStdout:
                print('API call is disabled')


    def getAllCategories(self):
        if self.enableStdout:
            print('\nFetching list of all categories...')
        self.apiURL = URL_BASE + URL_GET_ALL_CATEGORIES
        if self.enableStdout:
            print(self.apiURL)

        if self.enableAPICall is True:
            self.response = requests.get(url=self.apiURL)
            responseList = json.loads(self.response.content)
            return responseList
        else:
            return list()

if __name__ == '__main__':
    obj = API()                             # Create class object
    obj.getRandom()                         # Calling get API to fetch an entry in a random category

    # Getting and displaying the list of all categories
    categories = obj.getAllCategories()
    print(len(categories))

    # Getting a specific category entry
    obj.getEntry('business')