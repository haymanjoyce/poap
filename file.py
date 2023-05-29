import csv


class Temp:
    def __int__(self, file_name):
        self.file_name = file_name


def read_file(file_name):
    with open(file_name, 'r') as file_data:
        for line in csv.reader(file_data):
            print(line)

