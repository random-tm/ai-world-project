import os.path
import json
import txt
import csv


def loadfile(filepath):
    if not os.path.isfile(filepath):
        return "File Path is Empty"
    elif filepath.endswith("n"):
        json.loadjsonfile(filepath)
    elif filepath.endswith("t"):
        txt.loadtextfile(filepath)
    elif filepath.endswith("v"):
        csv.loadcsvfile(filepath)
    else:
        return "Unsupported file type"
    return
