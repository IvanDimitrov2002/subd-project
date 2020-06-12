from mysql.connector import Error
from database.connect_db import DB


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


def update_book(id, title, genre, isbn, date):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''UPDATE Books
                       SET Title = %s,
                           ISBN  = %s,
                           Genre = %s,
                           Date  = %s
                       WHERE Id = %s;'''
            conn.cursor().execute(query, (title, isbn, genre, date, id))

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


def update_author(id, title):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''UPDATE Books
                       SET Name = %s
                       WHERE Id = %s;'''
            conn.cursor().execute(query, (title, id))

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
            res = conn.cursor()
            res.execute(query, (auth_name, ))
            return res.fetchone()

        except Error as e:
            print(e)


def get_author_by_id(auth_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Authors
                       WHERE Id = %s;'''
            res = conn.cursor()
            res.execute(query, (auth_id, ))
            return res.fetchone()

        except Error as e:
            print(e)


def get_all_authors():
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Authors;'''
            res = conn.cursor()
            res.execute(query)
            return res.fetchall()

        except Error as e:
            print(e)


def get_all_books():
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books;'''
            res = conn.cursor()
            res.execute(query)
            return res.fetchall()

        except Error as e:
            print(e)


def get_book_by_id(book_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Id = %s;'''
            res = conn.cursor()
            res.execute(query, (book_id, ))
            return res.fetchone()

        except Error as e:
            print(e)


def get_book_by_title(title):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Title = %s;'''
            res = conn.cursor()
            res.execute(query, (title, ))
            return res.fetchone()

        except Error as e:
            print(e)


def get_books_by_substring(substring):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Title LIKE %s;'''
            res = conn.cursor()
            res.execute(query, ("%" + substring + "%", ))
            return res.fetchall()

        except Error as e:
            print(e)


def get_books_by_genre(genre):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT *
                       FROM Books
                       WHERE Genre = %s;'''
            res = conn.cursor()
            res.execute(query, (genre, ))
            return res.fetchall()

        except Error as e:
            print(e)


def get_books_by_auth_name(auth_name):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Books.Id, Books.ISBN, Books.Genre, Books.Title, Books.Date
                       FROM Authors
                       INNER JOIN AuthorsBooks
                       ON Authors.Id = AuthorsBooks.Auth_id
                       INNER JOIN Books
                       ON Books.Id = AuthorsBooks.Book_id
                       WHERE Name = %s;'''
            res = conn.cursor()
            res.execute(query, (auth_name, ))
            return res.fetchall()

        except Error as e:
            print(e)


def get_books_by_auth_id(auth_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Books.Id, Books.ISBN, Books.Genre, Books.Title, Books.Date
                       FROM Authors
                       INNER JOIN AuthorsBooks
                       ON Authors.Id = AuthorsBooks.Auth_id
                       INNER JOIN Books
                       ON Books.Id = AuthorsBooks.Book_id
                       WHERE Author.Id = %s;'''
            res = conn.cursor()
            res.execute(query, (auth_id, ))
            return res.fetchall()

        except Error as e:
            print(e)


def get_book_authors(book_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Authors.Id, Authors.Name
                       FROM Authors
                       INNER JOIN AuthorsBooks
                       ON Authors.Id = AuthorsBooks.Auth_id
                       INNER JOIN Books
                       ON Books.Id = AuthorsBooks.Book_id
                       WHERE Books.Id = %s;'''
            res = conn.cursor()
            res.execute(query, (book_id, ))
            return res.fetchall()

        except Error as e:
            print(e)


def get_author_books(author_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Books.Id, Books.ISBN, Books.Genre, Books.Title, Books.Date
                       FROM Authors
                       INNER JOIN AuthorsBooks
                       ON Authors.Id = AuthorsBooks.Auth_id
                       INNER JOIN Books
                       ON Books.Id = AuthorsBooks.Book_id
                       WHERE Author.Id = %s;'''
            res = conn.cursor()
            res.execute(query, (author_id, ))
            return res.fetchall()

        except Error as e:
            print(e)


def __get_book_id_by_title(book_title):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''SELECT Id
                       FROM Books
                       WHERE Title = %s;'''
            res = conn.cursor().execute(query, (book_title, )).fetchone()
            return res

        except Error as e:
            print(e)


def delete_book_by_title(book_title):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''DELETE
                       FROM Books
                       WHERE Id = %s;'''
            conn.cursor().execute(query, __get_book_id_by_title(book_title))
            conn.commit()

        except Error as e:
            conn.rollback()
            print(e)


def delete_book_by_id(book_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''DELETE
                       FROM Books
                       WHERE Id = %s;'''
            conn.cursor().execute(query, (book_id, ))
            conn.commit()
            return True

        except Error as e:
            conn.rollback()
            print(e)


def delete_author_by_id(author_id):
    with DB() as conn:
        conn.connect(database="Library")
        try:
            query = '''DELETE
                       FROM Authors
                       WHERE Id = %s;'''
            conn.cursor().execute(query, (author_id, ))
            conn.commit()
            return True

        except Error as e:
            conn.rollback()
            print(e)
