"""
=====================================
Title: Random Password Generator
Author: Micheal LeBlanc
Date: 03/31/2023
=====================================
"""

# Import Libraries
import string #for random password creation
import datetime #as a timestamp of when user/pass was create
import secrets
import sys

# Global data types
database = []


# Define functions
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

def exit_system():
    print("Thanks for trusting that your information is safe with Unsafe Database!")
    sys.exit()

def get_username():
    print("\nEnter a username to be entered into the database.")
    username = input("Username: ")

    if check_for_duplicates(database, username) == True:
        print(f"The username {username} is already taken. Choose another username.")
        get_username()
    else:
        user_pass = generate_password()
        append_to_database(username,user_pass)
    
    #Back to Main Menu
    core_iteration()

def check_for_duplicates(check_list, duplicate):
    is_duplicate = False
    #Checks each key at database index
    for dictionary_index in check_list:
        if duplicate in dictionary_index:
            is_duplicate = True
            # print("This username is taken.")
            return is_duplicate
    return is_duplicate

def append_to_database(uname, upass):
    entry = dict()
    entry[uname] = upass
    database.append(entry)
    print(f"{uname}'s password is: {upass}")

def generate_password():
    pass_inputs = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(pass_inputs) for i in range(12))
    return password

def lookup_username():
    print("\nEnter the username you are looking for.")
    lookup = input("User:")
    
    if check_for_duplicates(database, lookup):
        print(lookup, "was found in the database.")
    else:
        print(lookup, "was not found in the database.")

    #Back to Main Menu
    core_iteration()

def is_input_valid(check_input):
    valid_entries = ["1", "2", "e", "E"]
    if check_input in valid_entries:
        return True
    else:
        return False

# Starts program
core_iteration()