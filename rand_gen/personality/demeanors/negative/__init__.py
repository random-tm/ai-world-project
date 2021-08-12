from random import randrange
from rand_gen.personality.demeanors.demanor import Demeanor


class NegativeDemeanor(Demeanor):

    def generate_trait(self, trait):
        return randrange(0, 100) * trait

    def __init__(self, word_list):
        super().__init__()
        self.aggressive_trait = 0.8
        self.fear_trait = 0.2
        self.integrity_trait = 0.1
        self.intelligence_trait = 0.5
        self.word_list = word_list
        # If you want custom logic add the code here