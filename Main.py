"""
Interpreter Project
Author: 
Date: 4 March 2016
Version: 0.99
"""
from Controller import Controller


class Main:
    def __init__(self, path):
        self.myController = Controller(path)

if __name__ == '__main__':
    Main("TestData.csv")
