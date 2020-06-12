from flask import Flask, render_template, url_for, request
import database.create as database

from models.book import Book
from models.author import Author

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/books', methods=['GET', 'POST'])
def view_books():
    if request.method == 'GET':
        books = []
        req = request.args

        if req.get('search') == 'book':
            books = Book.find_by_substring(req.get('title'))
            if(books is None):
                books = Book.get_all_books()
            if(books is None):
                return render_template('index.html')
            return render_template('books.html', books=books)

        elif req.get('search') == 'genre':
            books = Book.find_by_genre(req.get('title'))
            if(books is None):
                books = Book.get_all_books()
            if(books is None):
                return render_template('index.html')
            return render_template('books.html', books=books)

        elif req.get('search') == 'author':
            books = Book.find_by_author(req.get('title'))
            if(books is None):
                books = Book.get_all_books()
            if(books is None):
                return render_template('index.html')
            return render_template('books.html', books=books)

    if request.method == 'POST':
        form = request.form
        if form["target"] == 'delete':
            if Book.delete_book_by_id(form["id"]):
                books = Book.get_all_books()
                if(books is None):
                    return render_template('index.html')
                return render_template('books.html', books=books)

        if form["target"] == 'update':
            book = Book.find_by_id(form['id'])
            if book:
                book.date = form['date']
                book.genre = form['genre']
                book.title = form['title']
                book.isbn = form['isbn']
                return render_template('books.html', books=book)
            else:
                books = Book.get_all_books()
                if not books:
                    return render_template('index.html')
                return render_template('books.html', books=books)


@app.route('/authors', methods=['GET', 'POST'])
def view_authros():
    if request.method == 'GET':
        authors = Author.get_all_authors()
        if(authors is None):
            return render_template('index.html')
        return render_template('authors.html', authors=authors)

    if request.method == 'POST':
        form = request.form
        if form["target"] == 'delete':
            if Author.delete_author_by_id(form["id"]):
                authors = Author.get_all_authors()
                if(authors is None):
                    return render_template('index.html')
                return render_template('authors.html', authors=authors)

        if form["target"] == 'update':
            auth = Author.find_by_id(form[id])
            if auth:
                auth.name = form['name']
                return render_template('authors.html',
                                       authors=auth)
            else:
                authors = Author.get_all_authors()
                if not authors:
                    return render_template('index.html')
                return render_template('authors.html',
                                       authors=authors)


if __name__ == '__main__':
    database.createDB()

    # books = [Book(None, "12319123", "Adventure", "Lady Midnight", "2020-03-13"),
    #          Book(None, "12314222", "Adventure", "Lord of Shadows", "2018-03-13"),
    #          Book(None, "54569123", "Info", "How to program", "2016-03-09"),
    #          Book(None, "12319123", "Info", "Giving you them", "2021-05-13")]

    # for book in books:
    #     book.add_book()

    app.run(debug=True)
