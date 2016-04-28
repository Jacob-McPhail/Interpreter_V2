import unittest
from Main import Main
from Model import Model



class UnitTest(unittest.TestCase):
    def test_file_input(self):
        self.myModel = Model()
        self.myModel.read_in_csv("testFileLoad.txt")
        self.expected = ['Hello', 'This', 'Is', 'A', 'Test']
        self.failUnlessEqual(self.myModel.get_data_set(), self.expected)

    def test_csv_file_input(self):
        self.myModel = Model()
        self.myModel.read_in_csv("TestData.csv")
        self.expected = 12
        self.failUnlessEqual(self.myModel.get_data_set().__len__(), self.expected)

    def test_washing_data(self):
        self.myModel = Model()
        # There are 5 errors so length should be cut down to 7 after washing
        self.myModel.read_in_csv("TestData.csv")
        self.expected = 7
        self.failUnlessEqual(self.myModel.wash_data().__len__(), self.expected)

