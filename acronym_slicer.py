# created on 15/4/22
# a simple code to find the abbreviation of a name
# I created this as I wanted to find the abbreviation of a name for my height calculator

def abbreviation():
    first_letter = (name[0])
    distance_of_space = (name.index(" "))
    if distance_of_space == 1:
        second_letter = (name[2])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 2:
        second_letter = (name[3])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 3:
        second_letter = (name[4])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 4:
        second_letter = (name[5])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 5:
        second_letter = (name[6])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 6:
        second_letter = (name[7])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 7:
        second_letter = (name[8])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 8:
        second_letter = (name[9])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 9:
        second_letter = (name[10])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 10:
        second_letter = (name[11])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 11:
        second_letter = (name[12])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")
    if distance_of_space == 12:
        second_letter = (name[13])
        print(f"WELCOME {first_letter.capitalize()}{second_letter.capitalize()}")

name = input("Enter your name: ")
