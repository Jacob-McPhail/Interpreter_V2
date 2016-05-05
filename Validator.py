import re

class Validator:
    def match_id(self, data):
        return re.match("^[A-Z][0-9]{3}$", data, flags=re.IGNORECASE)

    def match_gender(self, data):
        return re.match("(M|F)", data)


    def match_age(self, data):
        return re.match("[0-9]{1,2}$", data)

    def match_bmi(self, data):
        return re.match("[0-9]{3}$", data)


    def match_weight(self, data):
        return re.match("(Normal|Overweight|Obesity|Underweight)", data)

    def match_sales(self, data):
        return re.match("[0-9]{2,3}$", data)