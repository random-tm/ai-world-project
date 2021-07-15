import select_word


# Get random verb
def get_verb(chance):
    return select_word("verbs.csv", chance)