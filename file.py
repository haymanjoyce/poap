import csv


class Temp:
    def __int__(self, file_name):
        self.file_name = file_name


def read_file_csv(file_name: str) -> None:
    with open(file_name, 'r') as file_data:
        for line in csv.reader(file_data):
            print(line)


def read_file_json(file_name: str) -> None:
    pass


def save_file_csv(file_name: str) -> None:
    pass


def save_file_json(file_name: str) -> None:
    pass

