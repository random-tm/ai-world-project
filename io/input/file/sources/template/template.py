from io.input.file.loader.txt import load_text_file
import re


# Load template lines and words to replace using the pattern %word%
def load_template(template_path):
    file = load_text_file(template_path)
    words_needed = []
    text = []
    for line in file:
        text.append(line)
        if re.search("%", line):
            matcher = line.split("%")[1]
            words_needed.append(matcher)
    return text, words_needed
