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
        pakudex_size = len(self.species_name_list)
        return pakudex_size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.species_name_list:
            return None
        return self.species_name_list

    def get_stats(self, species):
        index_val = None
        ads_list = []
        found = False
        for i in range(len(self.species_name_list)):
            if self.species_name_list[i] == species:
                index_val = i
                found = True
        if not found:
            return None
        attack = Pakuri.get_attack(self.pakudex_obj_list[index_val])
        defense = Pakuri.get_defense(self.pakudex_obj_list[index_val])
        speed = Pakuri.get_speed(self.pakudex_obj_list[index_val])
        ads_list.append(attack)
        ads_list.append(defense)
        ads_list.append(speed)
        return ads_list

    def sort_pakuri(self):
        self.species_name_list.sort()
        return self.pakudex_obj_list.sort(key=lambda pakudex_obj_list: pakudex_obj_list.species)

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
        index_val = None
        found = False
        for i in range(len(self.species_name_list)):
            if self.species_name_list[i] == species:
                index_val = i
                found = True
        if not found:
            return False
        Pakuri.evolve(self.pakudex_obj_list[index_val])
        return True
