from database import database_funcs as database


class Author:
    def __init__(self, id, name, books=None):
        self.name = name
        self.id = id
        self.books = books

    def add_author(self):
        database.add_author(self.name)

    def update_author(self):
        database.update_book(self.id, self.name)

    @staticmethod
    def find_by_name(name):
        if not name:
            return None
        else:
            row = database.get_author_by_name(name)
            if row:
                return Author(*row)
            else:
                return None

    @staticmethod
    def find_by_id(id):
        if not id:
            return None
        else:
            row = database.get_author_by_id(id)
            if row:
                return Author(*row)
            else:
                return None

    @staticmethod
    def get_all_authors():
        rows = database.get_all_authors()
        if rows:
            return [Author(*row) for row in rows]
        else:
            return None

    @staticmethod
    def delete_author_by_id(id):
        return database.delete_author_by_id(id)
