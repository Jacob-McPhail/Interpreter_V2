import pickle
import re


class Filer:
    def __init__(self):
        self.data_set = []

    def add_new_data(self, new_array):
        # try catch if its a list
        self.data_set += new_array

    def read(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.data_set is not []:
            print("File Loaded!")

    def save_data(self, display_data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(display_data, f)

    def pickle_data(self, display_data):
        try:
            with open('data.pickle', 'rb') as f:
                display_data = pickle.load(f)
        except FileNotFoundError:
            print("Existing data not found.")
            return

    def getData(self):
        return self.data_set