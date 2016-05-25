from Filer import Filer


class CSVReader(Filer):
    def read(self, path):
        print("loading file...")
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        self.add_new_data(li)
        if self.data_set is not []:
            print("CSV File Loaded!")

