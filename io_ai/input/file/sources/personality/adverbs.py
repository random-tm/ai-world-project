import select_word


# Get random adverb
def get_adverbs(chance):
    return select_word("adverbs.csv", chance)