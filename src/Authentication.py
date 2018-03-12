import hashlib
import sqlite3
from sqlite3 import Error


def hash_credential(user_credential):
    credential = hashlib.sha512()
    credential.update(user_credential.encode('utf-8'))
    return credential.hexdigest()


def connect_to_user_db():
    conn = sqlite3.connect('../databases/users.db')
    return conn


def create_user_table(conn):
    c = conn.cursor()

    first_column = "username text NOT NULL UNIQUE"
    second_column = "password text NOT NULL"
    try:
        c.execute('CREATE TABLE users ({f}, {s})'.format(f=first_column, s=second_column))
        conn.commit()
    except sqlite3.OperationalError:
        print("users table already exists")


def add_login_credentials(conn, username, password):
    username_hash = hash_credential(username)
    password_hash = hash_credential(password)

    c = conn.cursor()
    try:
        c.execute('INSERT INTO users VALUES ("{f}", "{s}")'.format(f=username_hash, s=password_hash))
        conn.commit()
        # Auto-generate the various tables necessary

    except sqlite3.IntegrityError:
        print("This user already exists")


def validate_login_credentials(conn, username, password):
    username_hash = hash_credential(username)
    password_hash = hash_credential(password)

    c = conn.cursor()
    try:
        count = 0
        for line in c.execute('SELECT * FROM users WHERE username="{f}" AND password="{s}"'
                                      .format(f=username_hash, s=password_hash)):
            count += 1
        if count == 1:
            return True
        else:
            return False
    except Error:
        pass
    return False


def main():

    conn = connect_to_user_db()
    create_user_table(conn)
    validate_login_credentials(conn, "jtm002030203", "youdontneedtoknowthis")


main()
