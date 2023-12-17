import yaml
from pathlib import Path


class PathManager:

    def __init__(self):
        self.path = str()

    def open_config(self):
        try:
            with open(Path('config.yaml'), "r") as config:
                data = yaml.load(config, Loader=yaml.SafeLoader)
                print(data)
                print(Path('config.yaml'))
                print(Path.cwd())
        except FileNotFoundError:
            with open(Path('config.yaml'), "w") as config:
                config_dict = dict()
                config_dict['export_path'] = {'a': 0, 'b': 1}
                yaml.dump(config_dict, config)


def path_cleaner(file_name: str, file_type: str, location: str) -> str:
    clean_path = str()
    return clean_path


def clean_file_name():
    pass


def clean_file_type():
    pass


def clean_location():
    pass



