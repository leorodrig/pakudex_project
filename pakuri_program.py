# main driver program
# imports
from pakudex import Pakudex


# main function
def main():
    # print the welcome message
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    # prompt for capacity / display it
    capacity = int(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {capacity} species of Pakuri.\n")
    pakudex = Pakudex(capacity)
    start = True
    while start:
        user_input_menu = menu()
        if user_input_menu == 1:
            if not pakudex.species_name_list:
                print("No Pakuri in Pakudex yet!\n")
            else:
                number = 1
                print("Pakuri in Pakudex:")
                for name in pakudex.species_name_list:
                    print(f"{number}: {name}")
                    number += 1
                print("\n")
        elif user_input_menu == 2:
            species_user_inp = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species_user_inp)
            if stats is None:
                print("Error! No such Pakuri!\n")
            else:
                print(f"Species: {species_user_inp}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}\n")
        elif user_input_menu == 3:
            if pakudex.species_stored_count >= capacity:
                print("Error: Pakudex is full\n")
            else:
                species_to_add = input("Enter the name of the species to add: ")
                decider_val = pakudex.add_pakuri(species_to_add)
                if decider_val:
                    print(f"Pakuri species {species_to_add} successfully added!\n")
                else:
                    print("Error: Pakudex already contains this species!\n")
        elif user_input_menu == 4:
            species_to_evolve = input("Enter the name of species to evolve: ")
            evolver_val = pakudex.evolve_species(species_to_evolve)
            if not evolver_val:
                print("Error: No such Pakuri!\n")
            else:
                print(f"{species_to_evolve} has evolved!\n")
        elif user_input_menu == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted\n")
            pass
        elif user_input_menu == 6:
            start = False
        else:
            print("Unrecognized menu selection!")


# menu function
def menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")
    menu_ret = int(input("What would you like to do? "))
    return menu_ret


# if __name__ == "__main__"
if __name__ == "__main__":
    main()
