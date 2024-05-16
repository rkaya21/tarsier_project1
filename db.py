import sqlite3


def create_connection():
    conn = sqlite3.connect('customer.db')
    return conn


def signup(conn, name, surname, username, password):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM TBL_USERS WHERE username = ?', (username,))
    user_count = cursor.fetchone()[0]

    if user_count > 0:
        print("Username Taken.")
    else:
        try:
            cursor.execute("""
            INSERT INTO TBL_USERS (name, surname, username, password) VALUES (?, ?, ?, ?)"""
                           ,(name, surname, username, password))
            conn.commit()
            print("Successful")
        except sqlite3.Error as error:
            print("Error:", error)

def login(conn, username):
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT password, name, surname FROM TBL_USERS WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()

        if result is not None:
            password, name, surname = result
            print(f"Login is successful {name} {surname}")
        else:
            print("Login Fail.Incorrect username and password.")
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    finally:
        cursor.close()


def forgotpass(conn, username):
    cursor = conn.cursor()

    update_pass = input("Please update password: ")

    cursor.execute('UPDATE TBL_USERS SET password = ? WHERE username = ?', (update_pass, username))
    conn.commit()

    print("Password Update!")


def infoup(conn, username):
    cursor = conn.cursor()

    update_name = input("Please update name: ")
    update_surname = input("Please update surname: ")

    cursor.execute(
        'UPDATE TBL_USERS SET name = ? , surname = ? WHERE username = ?'
        ,(update_name, update_surname, username))
    conn.commit()
    print("Information Update!")
