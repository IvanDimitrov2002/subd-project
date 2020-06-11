from mysql.connector import Error

# import database.connect as database
from connect_db import DB


def createDB():
<<<<<<< HEAD
    with DB() as conn:
        try:
            conn.cursor().execute("CREATE DATABASE IF NOT EXISTS Library")
            conn.connect(database="Library")

            conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Authors(
                                Id INT AUTO_INCREMENT PRIMARY KEY,
                                Name VARCHAR(256)
                                );''')

            conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Books(
                                Id INT AUTO_INCREMENT PRIMARY KEY,
                                ISBN VARCHAR(17),
                                Genre VARCHAR(256),
                                Title VARCHAR(256),
                                Date DATE
                                );''')

            conn.cursor().execute('''CREATE TABLE IF NOT EXISTS AuthorsBooks(
                                Book_id INT,
                                Auth_id INT,
                                FOREIGN KEY (Book_id) REFERENCES Books(Id),
                                FOREIGN KEY (Auth_id) REFERENCES Authors(Id)
                                );''')

        except Error:
            print(Error)

=======
    conn = database.connect_to_DB()
    try:
        conn.cursor().execute("CREATE DATABASE IF NOT EXISTS Library")
        conn.connect(database="Library")

        conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Authors
                            (ID INT AUTO_INCREMENT PRIMARY KEY,
                            Name VARCHAR(256) );''')

        conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Books
                            (ID INT AUTO_INCREMENT PRIMARY KEY,
                            ISBN VARCHAR(17),
                            Genre VARCHAR(256),
                            Title VARCHAR(256),
                            Date DATE);''')

        conn.cursor().execute('''CREATE TABLE IF NOT EXISTS AuthorsBooks
                            (ID_b INT,
                            ID_auth INT,
                            FOREIGN KEY (ID_b) REFERENCES Books(ID),
                            FOREIGN KEY (ID_auth) REFERENCES Authors(ID));''')

    except Error:
        print(Error)

    finally:
        conn.close()
>>>>>>> 1a209497335d1a9cbc335699db92f584633c441d
