# Finished
import hashlib
import sqlite3
from sqlite3 import Error


def hash_credential(user_credential):
    credential = hashlib.sha512()
    credential.update(user_credential.encode('utf-8'))
    return credential.hexdigest()


def connect_to_db(database_name):
    conn = sqlite3.connect(database_name)
    return conn

def create_user_table(conn):
    c = conn.cursor()

    first_column = "username text NOT NULL UNIQUE"
    second_column = "password text NOT NULL"
    try:
        c.execute('CREATE TABLE users (?, ?)', (first_column, second_column))
        conn.commit()
    except sqlite3.OperationalError:
        pass


def add_login_credentials(conn, username, password):
    username_hash = hash_credential(username)
    password_hash = hash_credential(password)

    c = conn.cursor()
    try:
        c.execute('INSERT INTO users VALUES (?, ?)', (username_hash, password_hash))
        conn.commit()
        return True
        # Auto-generate the various tables necessary

    except sqlite3.IntegrityError:
        return False


def validate_login_credentials(conn, username, password):
    username_hash = hash_credential(username)
    password_hash = hash_credential(password)

    c = conn.cursor()
    try:
        count = 0
        for _ in c.execute('SELECT * FROM users WHERE username=? AND password=?', (username_hash, password_hash)):
            count += 1
        if count == 1:
            return True
        else:
            return False
    except Error:
        pass
    return False


def main():

    conn = connect_to_db('../databases/users.db')
    create_user_table(conn)
    validate_login_credentials(conn, "jtm002030203", "youdontneedtoknowthis")


main()
