# class describing an individual pokemon
class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = 0
        self.defense = 0
        self.speed = 0

    def get_species(self):
        return self.species

    def get_attack(self):
        self.attack = (len(self.species) * 7) + 9
        return self.attack

    def get_defense(self):
        self.defense = (len(self.species) * 5) + 17
        return self.defense

    def get_speed(self):
        self.speed = (len(self.species) * 6) + 13
        return self.speed

    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3
