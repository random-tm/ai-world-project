from io.input.file.sources.template.template import load_template
from io.input.file.sources.personality.word import select_word
from rand_gen.personality.personality import generate_persona
import re


def combine(template_path, file_path):
    text = ""
    # Take a template
    template, words_needed = load_template(template_path)
    # Generate a persona
    # TODO Make a dynamic demeanor
    max_chance = generate_persona("neutral")
    # Replace words in template
    for word in words_needed:
        word = select_word(file_path, max_chance)
        words_needed.append(word)
    # Format a log of text
    for line in template:
        text = text + line
        if re.search("%", line):
            text = words_needed[line] + text
    return text
