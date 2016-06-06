from Builder import Builder

class PersonBuilder(Builder):
    def __init__(self):
        self.id = ""
        self.gender = ""
        self.age = ""
        self.bmi = ""
        self.weight = ""
        self.sales = ""

    def build(self, newId, newGender, newAge, newBMI, newWeight, newSales):
        self.id = newId
        self.gender = newGender
        self.age = newAge
        self.bmi = newBMI
        self.weight = newWeight
        self.sales = newSales

    def get_id(self):
        return self.id

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_bmi(self):
        return self.bmi

    def get_weight(self):
        return self.weight

    def get_sales(self):
        return self.sales