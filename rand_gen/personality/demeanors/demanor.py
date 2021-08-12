from abc import ABC, abstractmethod


class Demeanor:

    # These are abstract
    aggressive_trait = 1
    fear_trait = 1
    integrity_trait = 1
    intelligence_trait = 1

    def __init__(self):
        self.__generate_persona_variance()

    def pick_word(self, word_type):
        return "Implement word"
        #TODO Hook up file load code

    @abstractmethod
    def generate_trait(self, value):
        return 1

    def __generate_aggressiveness(self):
        return self.generate_trait(self.aggressive_trait)

    def __generate_fear(self):
        return self.generate_trait(self.fear_trait)

    def __generate_integrity(self):
        return self.generate_trait(self.integrity_trait)

    def __generate_intelligence(self):
        return self.generate_trait(self.intelligence_trait)

    def __generate_persona_variance(self):
        self.aggressive_calc = self.__generate_aggressiveness()
        self.fear_calc = self.__generate_fear()
        self.integrity_calc = self.__generate_integrity()
        self.intelligence_calc = self.__generate_intelligence()