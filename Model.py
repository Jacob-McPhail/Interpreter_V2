import re
import pickle


class Model:
    def __init__(self, theFiler, theValidator):
        self.data_set = list()
        self.display_data = list()
        self.wrong_data = list()
        self.file_there = ""
        self.del_num_list = list()
        self.wrong_matching = []
        self.myFiler = theFiler
        self._ = theValidator

    def del_data(self):
        self.data_set = list()

    def get_data_set(self):
        return self.data_set

    def get_data(self):
        return self.display_data

    def read_in_csv(self, path):
        self.myFiler.read(path)
        self.toDataSet()
        self.wash_data()

    def remove_wrong(self, matching, index):
        inter = 0
        if matching is None:
            if inter == 0:
                self.del_num_list.insert(self.del_num_list.__sizeof__(), index)
                inter += 1

        return

    def toDataSet(self):
        self.data_set = self.myFiler.getData()

    def check_and_delete(self,index):
        for data in self.wrong_matching:
            if data == None:
                self.data_set.pop(index - 1)

    def wash_data(self):
        index = 0
        self.toDataSet()
        for i in self.data_set:
            tmp = self.data_set[index].split(',')
            index += 1
            num = 1
            matching = None
            self.display_data.insert(self.display_data.__sizeof__(), tmp)

            for j in range(0, len(tmp), 6):
                self.wrong_matching.append(self._.match_id(tmp[j]))
                self.wrong_matching.append(self._.match_gender(tmp[j + 1]))
                self.wrong_matching.append(self._.match_age(tmp[j + 2]))
                self.wrong_matching.append(self._.match_bmi(tmp[j + 3]))
                self.wrong_matching.append(self._.match_weight(tmp[j + 4]))
                self.wrong_matching.append(self._.match_sales(tmp[j + 5]))
                self.check_and_delete(index)
                self.wrong_matching.clear()

        self.del_num_list.reverse()
        for item in self.del_num_list:
            self.data_set.pop(item - 1)

        return self.data_set

    def read_in_csv(self, path):
        self.myFiler.read(path)

    def save_data(self):
        self.myFiler.save_data(self.display_data)

    def pickle_data(self):
        self.myFiler.pickle_data(self.display_data)

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
