from io.input.file.sources.personality.word import select_word


# Get random adverb
def get_adverb(chance):
    return select_word("adverbs.csv", chance)
