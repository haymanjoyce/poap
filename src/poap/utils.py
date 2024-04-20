import json


def store_path(name: str, path: str):
    config = {}
    try:
        with open('data/json/config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("No config file found. Creating a new one.")

    config[name] = path

    with open('data/json/config.json', 'w') as f:
        json.dump(config, f)
