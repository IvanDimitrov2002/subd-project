from database import database_funcs as database
from database.connect_db import DB
from mysql.connector import Error


class Book:
    def __init__(self, id, isbn, genre, title, date):
        self.id = id
        self.isbn = isbn
        self.genre = genre
        self.title = title
        self.date = date

    def add_book(self):
        with DB() as conn:
            conn.connect(database="Library")
            try:
                conn.cursor().execute('''
                    INSERT INTO Books
                    VALUES(NULL, %s, %s, %s, %s)
                ''', (self.isbn, self.genre, self.title, self.date))

            except Error as e:
                print(e)

    @staticmethod
    def find_by_id(id):
        if not id:
            return None
        else:
            row = database.get_book_by_id(id)
            if row:
                return Book(*row)
            else:
                return None

    @staticmethod
    def find_by_title(title):
        if not title:
            return None
        else:
            row = database.get_book_by_title(title)
            if row:
                return Book(*row)
            else:
                return None

    @staticmethod
    def find_by_genre(genre):
        if not genre:
            return None
        else:
            rows = database.get_books_by_genre(genre)
            if rows:
                return [Book(*row) for row in rows]
            else:
                return None

    @staticmethod
    def find_by_substring(substring):
        if not substring:
            return None
        else:
            rows = database.get_books_by_substring(substring)
            if rows:
                return [Book(*row) for row in rows]
            else:
                return None

    @staticmethod
    def get_all_books():
        rows = database.get_all_books()
        if rows:
            return [Book(*row) for row in rows]
        else:
            return None
