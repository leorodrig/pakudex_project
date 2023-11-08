# main driver program
# main function
def main():
    # print the welcome message
    print("Welcome to Pakudex: Tracker Extraordinare!")
    # prompt for capacity / display it
    capacity = input("Enter max capacity of the Pakudex: ")
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    start = True
    while start:
        user_input_menu = menu()
        print(user_input_menu)


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
