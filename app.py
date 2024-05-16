import char

from db import login, signup, create_connection, forgotpass, infoup

def print_menu():
    print("""
    1-Sign Up
    2-Login
    3-Forgot Password
    4-Update Information
    """)

def get_valid_choice():
    while True:
        choice = input("Please enter a number (1, 2, 3, or 4): ")
        if not choice.isdigit():
            print("Please enter a valid number.")
        else:
            choice = int(choice)
            if choice not in [1, 2, 3, 4]:
                print("Please enter a valid number.")
            else:
                return choice


def get_valid_input(prompt, special_characters):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Please enter a value.")
        elif any(char in user_input for char in special_characters):
            print("Please enter a value without special characters.")
        else:
            return user_input

special_characters = "!@#$%^&*()_+=-`~[]{}|\\<>,./?;:\"'"

while True:
    print_menu()
    choice = get_valid_choice() # choice from the menu

    conn = create_connection() # db.py => create connection function.This function connect databse

    if choice == 1: # The user sign up option.
        name = get_valid_input("Name: ", special_characters) # prompt => name
        if any(char.isdigit() for char in name): # not contain numbers
            print("Your name can't contains numbers.")
            continue

        surname = get_valid_input("Surname: ", special_characters) # prompt => surname
        if any(char.isdigit() for char in surname): # not contain numbers
            print("Your surname can't contains numbers.")
            continue

        username = get_valid_input("Username: ", special_characters) # prompt => username
        if username.isdigit(): # not contain numbers
            print("Your username can't be only numbers.")
            continue

        password = get_valid_input("Password: ", special_characters)
        '''
        Special characters should be included in the password.**Look Here**
        '''

        #save to database
        signup(conn, name, surname, username, password)

    elif choice == 2: # The user login option.
        username = input("Username: ")
        password = input("Password: ")

        #database
        login(conn, username)

    elif choice == 3: # option when the user forgets their password.
        username = input("Username: ")

        #database
        forgotpass(conn, username)

    elif choice == 4: # option to update information.
        username = input("Username: ")

        #database
        infoup(conn, username)

    else:
        print("Please enter a valid option.")

    conn.close() # Database close.
