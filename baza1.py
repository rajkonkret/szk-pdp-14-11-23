# baza sql w pythonie

import sqlite3

# biblioteka dla bazy sqlite

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')  # baza w pamieci
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład otwierania bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
