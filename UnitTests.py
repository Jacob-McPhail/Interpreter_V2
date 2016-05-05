import unittest
from Main import Main
from Model import Model
from Filer import Filer
from Validator import Validator


class UnitTest(unittest.TestCase):
    def test_file_input(self):
        self.myFiler = Filer()
        self.myValidator = Validator()
        self.myModel = Model(self.myFiler,self.myValidator)
        self.myFiler.read("TestData.csv")
        self.myModel.toDataSet()
        self.failIfEqual(self.myModel.get_data_set(), None)

    def test_csv_file_input(self):
        self.myFiler = Filer()
        self.myValidator = Validator()
        self.myModel = Model(self.myFiler,self.myValidator)
        self.myFiler.read("TestData.csv")
        self.expected = 12
        self.myModel.toDataSet()
        self.failUnlessEqual(self.myModel.get_data_set().__len__(), self.expected)

    def test_washing_data(self):
        # There are 5 errors so length should be cut down to 7 after washing
        self.myFiler = Filer()
        self.myValidator = Validator()
        self.myModel = Model(self.myFiler,self.myValidator)
        self.myFiler.read("TestData.csv")
        self.expected = 8
        self.myModel.toDataSet()
        self.failUnlessEqual(self.myModel.wash_data().__len__(), self.expected)

    def test_validator_id(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_id("D003")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_id("DDD03")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_validator_gender(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_gender("M")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_gender("G")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_validator_age(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_age("13")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_age("F")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_validator_bmi(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_bmi("235")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_bmi("F")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_validator_weight(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_weight("Normal")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_weight("F")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_validator_sales(self):
        self.myValidator = Validator()
        self.result = self.myValidator.match_sales("235")
        self.expected = None
        self.failIfEqual(self.result, self.expected)
        self.result = self.myValidator.match_sales("FED")
        self.expected = None
        self.failUnlessEqual(self.result, self.expected)

    def test_filer_read(self):
        self.myFiler = Filer()
        self.myFiler.read("TestData.csv")
        self.result = self.myFiler.getData()
        self.notExpected = None
        self.failIfEqual(self.result, self.notExpected)