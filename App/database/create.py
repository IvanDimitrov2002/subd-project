from mysql.connector import Error

from database.connect_db import DB


def createDB():
    with DB() as conn:
        try:
            conn.cursor().execute("CREATE DATABASE IF NOT EXISTS Library")
            conn.connect(database="Library")

            conn.cursor().execute('''
                CREATE TABLE IF NOT EXISTS Authors(
                    Id INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(256)
                );
            ''')

            conn.cursor().execute('''
                CREATE TABLE IF NOT EXISTS Books(
                    Id INT AUTO_INCREMENT PRIMARY KEY,
                    ISBN VARCHAR(17),
                    Genre VARCHAR(256),
                    Title VARCHAR(256),
                    Date DATE
                );
            ''')

            conn.cursor().execute('''
                CREATE TABLE IF NOT EXISTS AuthorsBooks(
                    Book_id INT,
                    Auth_id INT,
                    FOREIGN KEY (Book_id) REFERENCES Books(Id),
                    FOREIGN KEY (Auth_id) REFERENCES Authors(Id)
                );
            ''')

        except Error:
            print(Error)
