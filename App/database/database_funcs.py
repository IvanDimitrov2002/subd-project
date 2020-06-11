from mysql.connector import Error
from connect_db import DB


def add_book(title, genre, isbn, date):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''INSERT INTO Books
                       VALUES(NULL, %s, %s, %s, %s);'''
            conn.cursor().execute(query, (title, genre, isbn, date))

        except Error as e:
            conn.rollback()
            print(e)


def add_author(author_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''INSERT INTO Authors
                       VALUES(NULL, %s);'''
            conn.cursor().execute(query, (author_name, ))

        except Error as e:
            conn.rollback()
            print(e)


def link_author_with_book(auth_id, book_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''INSERT INTO AuthorsBooks
                       VALUES(%s, %s);'''
            conn.cursor().execute(query, (auth_id, book_id))

        except Error as e:
            conn.rollback()
            print(e)


def get_author_by_name(auth_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Authors
                       WHERE Name = %s;'''
            res = conn.cursor().execute(query, (auth_name, )).fetchone()
            return res

        except Error as e:
            print(e)


def get_book_by_id(book_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Id = %s;'''
            res = conn.cursor().execute(query, (book_id, )).fetchone()
            return res

        except Error as e:
            print(e)


def get_book_by_title(title):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Title = %s;'''
            res = conn.cursor().execute(query, (title, )).fetchone()
            return res

        except Error as e:
            print(e)


def get_books_by_genre(genre):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Genre = %s;'''
            res = conn.cursor().execute(query, (genre, )).fetchall()
            return res

        except Error as e:
            print(e)


def get_books_by_auth_name(auth_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Books.Id, Books.ISBN, Books.Genre, Books.Title, Books.Date
                       FROM Authors
                       INNER JOIN AuthorsBooks
                       ON Authors.Id = AuthorsBooks.Id_auth
                       INNER JOIN Books
                       ON Books.Id = AuthorsBooks.Id_b
                       WHERE Name = %s;'''
            res = conn.cursor().execute(query, (auth_name, )).fetchall()
            return res

        except Error as e:
            print(e)


def __get_book_id_by_name(book_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Id
                       FROM Books
                       WHERE Name = %s;'''
            res = conn.cursor().execute(query, (book_name, )).fetchone()
            return res

        except Error as e:
            print(e)


def delete_book_by_name(book_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''DELETE
                       FROM Books
                       WHERE Id = %s;'''
            conn.cursor().execute(query, __get_book_id_by_name(book_name))
            conn.commit()

        except Error as e:
            print(e)
