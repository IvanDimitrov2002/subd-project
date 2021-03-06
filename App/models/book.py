from database import database_funcs as database


class Book:
    def __init__(self, id, isbn, genre, title, date, authors=[]):
        self.id = id
        self.isbn = isbn
        self.genre = genre
        self.title = title
        self.date = date
        self.authors = authors

    def add_book(self, authors):
        database.add_book(self.isbn,
                          self.genre,
                          self.title,
                          self.date,
                          authors)

    def update_book(self):
        database.update_book(self.id,
                             self.title,
                             self.genre,
                             self.isbn,
                             self.date,
                             self.authors)

    def get_book_authors(self):
        authors = database.get_book_authors(self.id)
        if authors:
            return authors

        return None

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
    def find_by_author(author):
        if not author:
            return None
        else:
            rows = database.get_books_by_auth_name(author.name)
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

    @staticmethod
    def delete_book_by_id(id):
        return database.delete_book_by_id(id)
