# ******************************************************************************
# Author:           Proxima-L3
# Date:             August 16, 2020
# Description:      A program that simulates a suspect database search engine
# Input:            Suspect names or descriptors
# Output:           Suspect descriptions/descriptors or names
# Sources:          None. (Except minimal review from one of my Udemy courses)
# ******************************************************************************

# CONSTANTS
DATABASE = 1
NAME_SEARCH = 2
DESCRIPTOR_SEARCH = 3
QUIT = 4

def main():

    # variables
    menu_choice = 0
    first_name_list = ['Richard', 'Amanda', 'Michael', 'Christopher', 'Don',
                       'Teryl', 'Ben', 'Claudia', 'David', 'Joe', 'Jim']
    last_name_list = ['Anderson', 'Tapping', 'Shanks', 'Judge', 'Davis',
                      'Rothery', 'Browder', 'Black', 'Hewlett', 'Flanigan',
                      'Fish']
    gender_list = ['Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male',
                   'Female', 'Male', 'Male', 'Male']
    age_list = ['Older Adult', 'Adult', 'Adult', 'Adult', 'Senior', 'Adult',
                'Adult', 'Adult', 'Adult', 'Adult', 'Adult']
    height_list = ['Tall', 'Average', 'Tall', 'Tall', 'Short', 'Short', 'Tall',
                   'Average', 'Average', 'Tall', 'Tall']
    build_list = ['Average', 'Average', 'Fit', 'Heavy', 'Overweight', 'Fit',
                  'Fit', 'Slim', 'Overweight', 'Fit', 'Fit']
    eye_color_list = ['Brown', 'Green', 'Green', 'Brown', 'Blue', 'Brown',
                      'Blue', 'Grey', 'Green', 'Green', 'Blue']
    hair_style_list = ['Mullet', 'Short', 'Short', 'Bald', 'Bald', 'Short',
                       'Short', 'Long', 'Scruffy', 'Scruffy', 'Short']
    hair_color_list = ['Grey', 'Blonde', 'Brown', 'Black', 'Blonde', 'Blonde',
                       'Brown', 'Black', 'Brown', 'Black', 'Brown']
    glasses_list = ['False', 'False', 'True', 'False', 'False', 'True', 'False',
                    'False', 'True', 'False', 'False']
    descriptor_list = [first_name_list, last_name_list, gender_list, age_list,
                       height_list, build_list, eye_color_list,
                       hair_style_list, hair_color_list, glasses_list]

    # pre loop operations
    print("Suspect Database")
    input("\n(press enter to continue)")
    print("\033[H\033[J")

    # main program loop
    while menu_choice != QUIT:

        choice = 'yes'

        # displays main menu and options
        menu()
        menu_choice = get_menu_choice()

        # option pathways
        if menu_choice == DATABASE:
            display_database(first_name_list, descriptor_list)
        elif menu_choice == NAME_SEARCH:
            while choice == 'yes':
                suspect_index, first_name, last_name = \
                    name_search(first_name_list, last_name_list)
                retrieve_suspect(suspect_index, first_name,
                                 last_name, descriptor_list)
                choice = continue_searching()
        elif menu_choice == DESCRIPTOR_SEARCH:
            descriptor_search(descriptor_list, first_name_list, last_name_list)
        else:
            menu_choice = QUIT

    print("\n\nGoodbye!")


# FUNCTIONS

# This function displays the main menu
def menu():

    print("\033[H\033[J")
    print("1: Database\n2: Search by Name\n3: Search by Descriptors\n4: Quit")


# This function accepts the user menu choice and returns it
def get_menu_choice():

    while True:
        try:
            option = int(input("\n\nEnter option: "))
            if 0 < option < 5:
                break
            else:
                print("Invalid option.")
        except:
            print("Invalid option.")
    return option


# This function displays the suspect database
def display_database(first_name_list, descriptor_list):

    print("\033[H\033[J")
    print("Suspect Database\n")
    print("First Name\tLast Name\tGender\tAge Range\tHeight\tBuild\tEye Color"
          "\tHair Style\tHair Color\tGlasses\n")

    suspect_counter = 0

    for index in range(len(first_name_list)):

        suspect_descriptor_string = ''

        for descriptor in descriptor_list:
            suspect = f"{descriptor[suspect_counter]}\t"
            suspect_descriptor_string += suspect
        print(suspect_descriptor_string)

        suspect_counter += 1

    input("\n\n(press enter to return to main menu)")


# This function allows the user to search the database for a suspect. If
# the suspect is in the database, the suspect's names and index location
# are returned
def name_search(first_name_list, last_name_list):

    print("\033[H\033[J")
    print("Search By Name\n")

    f_name = input("Please enter the first name of suspect: ")
    l_name = input("Please enter the last name of suspect: ")

    index = 0
    for first_name in first_name_list:

        last_name = last_name_list[index]

        if f_name.lower() == first_name.lower() and \
                l_name.lower() == last_name.lower():
            suspect_index = first_name_list.index(first_name)

            return suspect_index, first_name, last_name
        elif first_name_list.index(first_name) == 10:
            return "null", "null", "null"

        index += 1


# This function accepts the info returned by the name_search function and
# prints the suspects descriptors
def retrieve_suspect(suspect_index, first_name, last_name, descriptor_list):

    if suspect_index != "null":

        suspect_descriptor_string = ''

        print(f"\n\n{first_name} {last_name}:\n")
        print("\tGender\tAge Range\tHeight\tBuild\tEye Color\tHair Style"
              "\tHair Color\tGlasses\n")
        for descriptor in descriptor_list[2:10]:
            suspect = f"{descriptor[suspect_index]}\t"
            suspect_descriptor_string += suspect
        print(f"\t{suspect_descriptor_string}")
    else:
        print("\n\nSuspect Not in Database.")


# This function accepts user input that will later determine whether to
# continue allowing the user to search by name or to return to the main menu
def continue_searching():

    while True:
        continue_choice = input("\n\nWould you like to search another name? "
                                "(yes/no): ")

        if continue_choice in ['yes', 'no']:
            return continue_choice
        else:
            print("Invalid option.")


# This function allows the user to search a suspect by descriptors then
# prints all suspect that have at least a 50% match rate
def descriptor_search(descriptor_list, first_name_list, last_name_list):

    print("Search By Descriptors\n")
    print("Please fill out descriptors to the best of your abilities\n")

    gender = input("Gender: ")
    age = input("Age Range (young adult/adult/older adult/senior): ")
    height = input("Height (tall/average/short): ")
    build = input("Build (slim/average/fit/heavy/overweight): ")
    eye_color = input("Eye Color: ")
    hair_style = input("Hair Style: ")
    hair_color = input("Hair Color: ")
    glasses = input("Glasses (true/false): ")
    form = [gender, age, height, build, eye_color, hair_style, hair_color,
            glasses]

    input_counter = 0
    match_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for descriptor in descriptor_list[2:10]:

        suspect_index = 0
        for item in descriptor:
            if form[input_counter].lower() == item.lower():
                match_list[suspect_index] += 1

            suspect_index += 1

        input_counter += 1

    for item in match_list:
        match_list[match_list.index(item)] = (item/8) * 100

    print("\n\nMatches:\n")

    suspect_index = 0
    matches = 0

    for item in match_list:
        if item >= 50:
            first_name = first_name_list[suspect_index]
            last_name = last_name_list[suspect_index]
            suspect_match = f"{first_name} {last_name} - {item:.1f}% match"
            print(suspect_match)
            matches += 1

        suspect_index += 1

    if matches == 0:
        print("No Matches.")

    input("\n\n(press enter to return to the main menu)")




main()
