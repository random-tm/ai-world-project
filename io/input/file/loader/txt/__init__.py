def load_text_file(file_path):
    with open(file_path) as file:
        content = file.read()
    file.close()
    return file_path.name, content
