import json

from src.poap import CONFIG_PATH


def store_path(name: str, path: str):
    config = {}
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("No config file found. Creating a new one.")

    config[name] = path

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


def get_path(name: str):
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            return config.get(name)
    except FileNotFoundError:
        print("No config file found.")
        return None
