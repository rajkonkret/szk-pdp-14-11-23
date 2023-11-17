# baza sql w pythonie

import sqlite3

# biblioteka dla bazy sqlite

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')  # baza w pamieci
    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_data DATETIME,
    salary REAL NOT NULL);
     '''

    with open('tables.sql', "r") as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")

    # cursor.execute(query)
    # sql_connection.commit()

    cursor.executescript(sql_script)

except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
