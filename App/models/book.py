from database import database_funcs as database


class Book:
    def __init__(self, title, genre, date, isbn, id=None):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.date = date
        self.genre = genre

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
            row = database.get_books_by_genre(genre)
            if row:
                return Book(*row)
            else:
                return None
