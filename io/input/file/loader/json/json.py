import os.path
import json


def loadjsonfile(filepath):
    with open(filepath) as file:
        content = json.loadfile(filepath)
    file.close()
    return filepath.name, content
