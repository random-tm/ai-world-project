import csv


def load_csv_file(file_path):
    with open(file_path) as file:
        content = csv.reader(file_path)
    file.close()
    return file_path.name, content
