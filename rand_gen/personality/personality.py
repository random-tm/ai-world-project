def generate_persona(type):
    if type == "Negative":
        return DemeanorNegative()
    elif type == "Neutral":
        return DemeanorNeutral()
    elif type == "Positive":
        return DemeanorPositive()
    else:
        random_persona = randrange(0,3)
        if random_persona == 0:
            return DemeanorNegative()
        elif random_persona == 1:
            return DemeanorNeutral()
        else:
            return DemeanorPositive()