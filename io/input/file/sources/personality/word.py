import random
from io.input.file.loader.csv import load_csv_file

# Return word structure
def load_word(file_path):
    content = load_csv_file(file_path)[1]
    words = []
    for line in content:
        line_parts = line.split(":")
        # Assume: word:chance
        words[line_parts[0]] = line_parts[1]
    return words


# Select a random word from the available list
def select_word(file_path, max_chance):
    words = load_word(file_path)
    random.shuffle(words)
    for word in words:
        chance = words[word]
        if chance <= max_chance:
            return word
