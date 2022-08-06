# Author: Fransiskus Agapa

the_pet = lambda name, color: name + " - " + color

print("\n== Pet Database ==")
print("1. Input data")
print("2. Output data")
print("e. Exit")
choice = input("choice: ").lower()  # user input to lower case - while-loop condition becomes simpler

pets = ()

while choice != 'e':
    if choice == '1':
        print("\n -- Input data --")
        pet_name = input("Input name of a pet: ").capitalize()
        if pet_name.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            pet_color = input("Input the color of the pet: ").capitalize()
            if pet_color.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                pet = the_pet(pet_name, pet_color)
                pets = pets + (pet,)       # add item to tuple
                print("\n[ Data updated ]")

    elif choice == '2':
        print("\n -- Output data --")
        to_output = input("Would you like to sort the output (yes/no): ").lower()
        if to_output == "yes":
            print("")                           # create new line
            sorted_pet = sorted(pets)           # can't use sort with tuple so make it list first
            for i in sorted_pet:
                print(i)

        elif to_output == "no":
            print("")
            for i in pets:
                print(i)

        else:
            print("\n[ Invalid response ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Pet Database ==")
    print("1. Input data")
    print("2. Output data")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
