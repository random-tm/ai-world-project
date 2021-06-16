import Demeanor

def generate_trait(trait):
    return randrange(0, 100) * trait

class PositiveDemeanor(Demeanor):

    def __init__(self, word_list):
        self.aggressive_trait = 0.2
        self.fear_trait = 0.2
        self.integrity_trait = 0.5
        self.intelligence_trait = 0.3
        self.word_list = word_list
        # If you want custom logic add the code here