from mysql.connector import Error

import connect as database

# CREATE DB IF NOT EXISTS AND ONE TABLE FOR
# Authors, ONE FOR BOOKS
# AND ONE TABLE TO REFERENCE THEM


def createDB():
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
