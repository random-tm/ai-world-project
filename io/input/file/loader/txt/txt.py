import os.path


def loadtextfile(filepath):
    with open(filepath) as file:
        content = file.read()
    file.close()
    return filepath.name, content
