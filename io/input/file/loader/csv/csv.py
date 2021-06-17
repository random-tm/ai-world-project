import os.path
import csv


def loadcsvfile(filepath):
    with open(filepath) as file:
        content = csv.reader(filepath)
    file.close()
    return filepath.name, content
