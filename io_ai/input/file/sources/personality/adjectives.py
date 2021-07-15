import select_word


# Get random adjective
def get_adjective(chance):
    return select_word("adjectives.csv", chance)