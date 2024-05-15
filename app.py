from db import login, signup, create_connection, forgotpass, infoup


def print_menu():
    print("""
    1-Sign Up
    2-Login
    3-Forgot Password
    4-Update Information
    """)

while True:
    print_menu()
    choice = int(input("Please enter number: "))

    if choice == 1:
        conn = create_connection()

        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        password = input("Password: ")
        # şifre kontrolu
        # 2.alan şifre için
        # password:  123
        # re-password: 123

        signup(conn, name, surname, username, password)
        conn.close()
    elif choice == 2:
        conn = create_connection()

        username = input("Username:")
        password = input("Password:")

        login(conn, username)
        conn.close()
    elif choice == 3:
        conn = create_connection()

        username = input("Username: ")

        forgotpass(conn, username)
        conn.close()
    elif choice == 4:
        conn = create_connection()

        username = input("Username: ")

        infoup(conn, username)
        conn.close()
    else:
        print("Please enter the required information.")


"""
1-) Login => Logged-in User Profile Screen
2-) User Register Screen
3-) Forgot Password Screen 
4-) Update Information Screen
"""