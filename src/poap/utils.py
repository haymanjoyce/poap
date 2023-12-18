import yaml
from pathlib import Path


class PathManager:

    def __init__(self):
        self.path = str()
        self.config_dict = get_config_dict()


def get_config_dict():
    try:
        with open(Path('config.yaml'), "r") as config_file:
            config_dict = yaml.load(config_file, Loader=yaml.SafeLoader)
            return config_dict
    except FileNotFoundError:
        with open(Path('config.yaml'), "w") as config_file:
            config_dict = dict()
            config_dict['export_path'] = {'location': '', 'name': '', 'type': ''}
            config_dict['import_path'] = {'location': '', 'name': '', 'type': ''}
            yaml.dump(config_dict, config_file)
            return config_dict

