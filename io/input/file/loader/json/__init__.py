import json


def load_json_file(file_path):
    with open(file_path) as file:
        content = json.load(file_path)
    file.close()
    return file_path.name, content
