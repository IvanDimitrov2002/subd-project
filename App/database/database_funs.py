from mysql.connector import Error

import database.connect as database


def create_conn():
    conn = database.connect_to_DB()
    conn.connect(database="Library")
    return conn


def insert_book(book):
    conn = create_conn()
    try:
        sql = '''INSERT INTO Books(NULL, Title,Genre, ISBN, DATE)
        VALUES(%s, %s, %s);'''
        conn.cursor().execute(sql, book)
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def insert_author(author):
    conn = create_conn()
    try:
        sql = '''INSERT INTO Authors(NULL, Name)
        VALUES(%s);'''
        conn.cursor().execute(sql, author)
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def connect_author_wiht_book(id_b, id_auth):
    conn = create_conn()
    try:
        sql = '''INSERT INTO AuthorsBooks(ID_auth, ID_b) VALUES(%s, %s);'''
        conn.cursor().execute(sql, id_auth, id_b)
        conn.commit()

    except Error as e:
        conn.rollback()
        print(e)

    finally:
        conn.close()


def extract_author(name):
    conn = create_conn()
    try:
        sql = 'SELECT Name, Id FROM Authors WHERE Name = %s;'
        result = conn.cursor()
        result.execute(sql, (name, ))
        return result.fetchone()

    except Error as e:
        print(e)

    finally:
        conn.close()


def extract_book(title):
    conn = create_conn()
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


def extract_genre_books(genre):
    conn = create_conn()
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


def find_books(name):
    conn = create_conn()
    try:
        sql = '''SELECT Books.Title, Books.Genre, Books.Date, Books.ISBN
        FROM Authors INNER JOIN AuthorsBooks
        ON Authors.ID = AuthorsBooks.ID_auth INNER JOIN Books
        ON Books.ID = AuthorsBooks.ID_b
        WHERE Name = %s;'''
        result = conn.cursor()
        result.execute(sql, (name, ))
        return result.fetchall()

    except Error as e:
        print(e)

    finally:
        conn.close()



