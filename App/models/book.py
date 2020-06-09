from database import database_funs as database


class Book:
    def __init__(self, title, genre, date, isbn, id=None):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.date = date
        self.genre = genre

    @staticmethod
    def find_by_title(title):
        if not title:
            return None
        else:
            row = database.extract_book(title)
            if row:
                return Book(*row)
            else:
                return None
