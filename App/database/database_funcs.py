from mysql.connector import Error
import database.connect as database


def __create_conn():
    conn = database.connect_to_DB()
    conn.connect(database="Library")
    return conn


def add_book(title, genre, isbn, date):
    conn = __create_conn()
    try:
        sql = '''INSERT INTO Books(ID, Title, Genre, ISBN, Date)
        VALUES(NULL, %s, %s, %s, %s);'''
        conn.cursor().execute(sql, (title, genre, isbn, date))
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def add_author(author):
    conn = __create_conn()
    try:
        sql = '''INSERT INTO Authors(ID, Name)
        VALUES(NULL, %s);'''
        conn.cursor().execute(sql, (author, ))
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def link_author_with_book(auth_id, book_id):
    conn = __create_conn()
    try:
        sql = '''INSERT INTO AuthorsBooks(ID_auth, ID_b) VALUES(%s, %s);'''
        conn.cursor().execute(sql, (auth_id, book_id))
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def get_author_by_name(auth_name):
    conn = __create_conn()
    try:
        sql = 'SELECT Name, ID FROM Authors WHERE Name = %s;'
        result = conn.cursor()
        result.execute(sql, (auth_name, ))
        return result.fetchone()

    except Error as e:
        print(e)

    finally:
        conn.close()


def get_book_by_title(title):
    conn = __create_conn()
    try:
        sql = '''SELECT Title, Genre, Date, ISBN, ID
            FROM Books WHERE Title = %s;'''
        result = conn.cursor()
        result.execute(sql, (title, ))
        return result.fetchone()

    except Error as e:
        print(e)

    finally:
        result.close()
        conn.close()

def get_book_by_title(title):
    conn = __create_conn()
    try:
        sql = '''SELECT Title, Genre, Date, ISBN, ID
            FROM Books;'''
        result = conn.cursor()
        result.execute(sql, (title, ))
        return result.fetchall()

    except Error as e:
        print(e)

    finally:
        result.close()
        conn.close()


def get_books_by_genre(genre):
    conn = __create_conn()
    try:
        sql = '''SELECT Title, Genre, Date, ISBN, ID
                FROM Books WHERE Genre = %s;'''
        result = conn.cursor()
        result.execute(sql, (genre, ))
        return result.fetchall()

    except Error as e:
        print(e)

    finally:
        result.close()
        conn.close()


def get_books_by_auth_name(auth_name):
    conn = __create_conn()
    try:
        sql = '''SELECT Books.Title, Books.Genre, Books.Date, Books.ISBN
                FROM Authors INNER JOIN AuthorsBooks
                ON Authors.ID = AuthorsBooks.ID_auth INNER JOIN Books
                ON Books.ID = AuthorsBooks.ID_b
                WHERE Authors.Name = %s;'''
        result = conn.cursor()
        result.execute(sql, (auth_name, ))
        return result.fetchall()

    except Error as e:
        print(e)

    finally:
        result.close()
        conn.close()


def delete_book_by_name(id):
    conn = __create_conn()
    try:
        sql = '''DELETE FROM Books WHERE Name = %s;'''
        conn.cursor().execute(sql, (book_name, ))
        conn.commit()

    except Error as e:
        print(e)

    finally:
        conn.close()

def delete_book_by_name(id):
    conn = __create_conn()
    try:
        sql = '''DELETE FROM Books WHERE ID = %s;'''
        conn.cursor().execute(sql, (book_name, ))
        conn.commit()

    except Error as e:
        print(e)

    finally:
        conn.close()
