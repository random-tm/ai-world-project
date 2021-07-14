import load_csv_file


# Return word structure
def load_word(file_path):
    content = load_csv_file(file_path)[1]
    words = []
    for line in content:
        line_parts = line.split(":")
        # Assume: word:chance
        words[line_parts[0]] = line_parts[1]
    return words


def select_word(file_path, max_chance):
    words = load_word(file_path)
    words.shuffle()
    for word in words:
        chance = words[word]
        if chance <= max_chance:
            return word
