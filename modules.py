import json

def load_json(path):
    with open(path, encoding='utf-8') as json_file:
        return json.load(json_file)