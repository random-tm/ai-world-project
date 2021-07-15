import select_word


# Get random verb
def get_verbs(chance):
    return select_word("verbs.csv", chance)