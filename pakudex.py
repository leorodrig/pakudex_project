# class describing the Pokédex as a whole
# import pakuri
from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakudex_obj_list = []
        self.species_name_list = []
        self.species_stored_count = 0

    def get_size(self):
        pass

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        pass

    def get_stats(self, species):
        pass

    def sort_pakuri(self):
        pass

    def add_pakuri(self, species):
        for name in self.species_name_list:
            if name == species:
                return False
        if self.species_stored_count >= self.capacity:
            return False
        new_species = Pakuri(species)
        self.pakudex_obj_list.append(new_species)
        self.species_name_list.append(new_species)
        self.species_stored_count += 1
        return True

    def evolve_species(self, species):
        pass
