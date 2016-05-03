"""
    >>> myModel = Model()
    >>> myModel.read_in_csv("TestData.csv")
    loading file...
    File Loaded!

    >>> integer = myModel.wash_data().__len__()
    >>> integer
    7


"""
import re
import pickle

#Large Class
class Model:
    def __init__(self):
        self.data_set = list()
        self.display_data = list()
        self.wrong_data = list()
        self.file_there = ""

    def add_new_data(self, new_array):
        # try catch if its a list
        self.data_set += new_array

    def del_data(self):
        self.data_set = list()

    def get_data_set(self):
        return self.data_set

    def get_data(self):
        return self.display_data

    # Single Responsibility

    def read_in_csv(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.data_set is not []:
            print("File Loaded!")
        self.wash_data()
    #Large Method
    def wash_data(self):
        index = 0
        del_num_list = list()
        for i in self.data_set:
            tmp = self.data_set[index].split(',')
            index += 1
            num = 1
            inter = 0
            matching = None

            self.display_data.insert(self.display_data.__sizeof__(), tmp)
            for data in tmp:
                if num == 1:
                    matching = re.match("^[A-Z][0-9]{3}$", data, flags=re.IGNORECASE)
                elif num == 2:
                    matching = re.match("(M|F)", data)
                elif num == 3:
                    matching = re.match("[0-9]{1,2}$", data)
                elif num == 4:
                    matching = re.match("[0-9]{3}$", data)
                elif num == 5:
                    matching = re.match("(Normal|Overweight|Obesity|Underweight)", data)
                elif num == 6:
                    matching = re.match("[0-9]{2,3}$", data)
                num += 1
                if matching is None:
                    self.wrong_data.insert(self.wrong_data.__sizeof__(), data)
                    if inter == 0:
                        del_num_list.insert(del_num_list.__sizeof__(), index)
                        inter += 1
                    # Saving the specific data that's wrong - can change to whole line if we want

                    # Storing which indexes of data set have incorrect data.
                    # To either remove it entirely or take out of displaying

        del_num_list.reverse()
        for item in del_num_list:
            self.data_set.pop(item - 1)
            
        return self.data_set

    def save_data(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.display_data, f)

    def pickle_data(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.display_data = pickle.load(f)
        except FileNotFoundError:
            print("Existing data not found.")
            return

    def get_sales(self):
        result = []
        for i in self.display_data:
            result.append(int(i[3]))
        return result

    def get_weight(self):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in self.display_data:
            if i[4] == 'Normal':
                normal += 1
            elif i[4] == 'Overweight':
                over += 1
            elif i[4] == 'Obesity':
                obese += 1
            elif i[4] == 'Underweight':
                under += 1
        return [normal, over, obese, under]

    def get_gender(self):
        m = 0
        f = 0
        for i in self.display_data:
            if i[1] == 'M':
                m += 1
            elif i[1] == 'F':
                f += 1
        return [m, f]

