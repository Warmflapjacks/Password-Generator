"""
=====================================
Title: Random Password Generator
Author: Micheal LeBlanc
Date: 03/31/2023
=====================================
"""

# Import Libraries
import string #for random password creation
import secrets
import sys

# Global data types
database = []


# Define functions
# The main menu of the program
def core_iteration():
    print("\n******Welcome to the Unsafe Database******")
    print("Select a number from the Main Menu:")
    print("1: Enter username for a password to be assigned.")
    print("2: Lookup a username")
    print("E: Exit the program")
    user_input = input("\nSelection:")

    if(is_input_valid(user_input)):
        if user_input == "E" or "e":
            get_user_input(user_input.upper())
        else:
            get_user_input(user_input) 
    else:
        print("Invalid selection.. Returning to Main Menu")
        core_iteration()
    
def get_user_input(selection):
    match selection:
        case "1":
            get_username()
        case "2":
            lookup_username()
        case "E":
            exit_system()

# Stops the program on request
def exit_system():
    print("Thanks for trusting that your information is safe with Unsafe Database!")
    sys.exit()

# Takes username input
def get_username():
    print("\nEnter a username to be entered into the database.")
    username = input("Username: ")

    if check_for_duplicates(database, username) == True:
        print(f"The username {username} is already taken. Choose another username.")
        get_username()
    else:
        date_of_birth = enter_user_birthday()
        user_pass = generate_password()
        append_to_database(username, user_pass, date_of_birth)
    
    #Back to Main Menu
    core_iteration()

# Checks if a username is already in the database so an entry can be entered
def check_for_duplicates(check_list, duplicate):
    is_duplicate = False
    #Checks each key at database index
    for dictionary_index in check_list:
        if duplicate in dictionary_index:
            is_duplicate = True
            return is_duplicate
    return is_duplicate

# Adds the username and pass as a dictionary into the database
def append_to_database(uname, upass, dob):
    entry = dict()
    entry[uname] = upass
    entry["DOB"] = dob
    database.append(entry)
    print(f"{uname}'s password is: {upass}")

# Generates the random password of characters and integers
def generate_password():
    pass_inputs = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(pass_inputs) for i in range(12))
    return password

# Checks if the username is already in the database
def lookup_username():
    print("\nEnter the username you are looking for.")
    lookup = input("User:")
    
    if check_for_duplicates(database, lookup):
        print(lookup, "was found in the database.")
    else:
        print(lookup, "was not found in the database.")

    #Back to Main Menu
    core_iteration()

# Determines if the user selection at main menu is a valid option
def is_input_valid(check_input):
    valid_entries = ["1", "2", "e", "E"]
    if check_input in valid_entries:
        return True
    else:
        return False

def enter_user_birthday():
    print("\nEnter your date of birth in the format MM-DD-YYYY. Do not include hyphens.")
    birthday = input("Date of Birth:")

    return birthday

# Starts program
core_iteration()

"""
====================================
Additional things to add
- Require birthday as a verification after entering username since passwords are random and arent expected to be remembered
    -100% need exception handling
- The option to see password if found in the database
    Require entering birthday as verification
- The ability to change password if found in database
    Require entering birthday as verification
-Current date/time when logging in
-Date/Time user was added into database
===================================
"""