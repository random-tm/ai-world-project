from random import randrange
from rand_gen.personality.demeanors.negative import NegativeDemeanor
from rand_gen.personality.demeanors.neutral import NeutralDemeanor
from rand_gen.personality.demeanors.positive import PositiveDemeanor


def generate_persona(demeanor_type):
    if demeanor_type == "Negative":
        return NegativeDemeanor()
    elif demeanor_type == "Neutral":
        return NeutralDemeanor()
    elif demeanor_type == "Positive":
        return PositiveDemeanor()
    else:
        random_persona = randrange(0, 3)
        if random_persona == 0:
            return NegativeDemeanor()
        elif random_persona == 1:
            return NeutralDemeanor()
        else:
            return PositiveDemeanor()