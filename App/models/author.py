from database import database_funcs as database


class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

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
