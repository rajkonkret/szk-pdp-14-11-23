# baza sql w pythonie
# C, R, U, D
import sqlite3

# biblioteka dla bazy sqlite

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')  # baza w pamieci

    insert = '''
    INSERT INTO software (id,name,price) VALUES(1, 'Python', 200);
    '''
    select = '''
    SELECT * FROM software WHERE id=1;'''
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")

    update = '''
    UPDATE software SET price=2000 WHERE id=1;
    '''

    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 200.0)
    # cursor.execute(insert)
    # sql_connection.commit()
    # cursor.execute(update)  # (1, 'Python', 2000.0)
    # sql_connection.commit()
    cursor.execute(delete)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Bład otwierania bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
