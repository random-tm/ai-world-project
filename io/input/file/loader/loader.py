import os.path
from io.input.file.loader.json import load_json_file
from io.input.file.loader.txt import load_text_file
from io.input.file.loader.csv import load_csv_file


def loadfile(file_path):
    if not os.path.isfile(file_path):
        return "File Path is Empty"
    elif file_path.endswith("n"):
        load_json_file(file_path)
    elif file_path.endswith("t"):
        load_text_file(file_path)
    elif file_path.endswith("v"):
        load_csv_file(file_path)
    else:
        return "Unsupported file type"
    return
