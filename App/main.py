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
    books = None
    if request.method == 'GET':
        req = request.args

        if not req.get('title') and req.get('title') != "":
            books = Book.find_by_substring(req.get('title'))

        elif not req.get('genre') and req.get('genre') != "":
            books = Book.find_by_genre(req.get('genre'))

        elif not req.get('author') and req.get('author') != "":
            books = Book.find_by_author(req.get('author'))

    if request.method == 'POST':
        if request.form["target"] == 'delete':
            Book.delete_book_by_id(request.form["id"])

    if not books:
        books = Book.get_all_books()

    if books:
        return render_template('books.html', books=books)

    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def update_book():
    books = None
    book = None
    if request.method == 'GET':
        book = Book.find_by_id(request.args.get('id'))

    if request.method == 'POST':
        form = request.form
        book = Book.find_by_id(form('id'))

        if book:
            book.date = form['date']
            book.genre = form['genre']
            book.isbn = form['isbn']
            book.title = form['title']
            book.update_book()

    if book:
        return render_template('books.html', books=[book])

    books = Book.get_all_books()
    if books:
        return render_template('books.html', books=books)

    return render_template('index.html')


@app.route('/authors', methods=['GET', 'POST'])
def view_authros():
    authors = None
    if request.method == 'GET':
        req = request.args

        if not req.get('name') and req.get('name') != "":
            authors = Book.find_by_author(req.get('name'))

        authors = Author.get_all_authors()
        if(authors):
            return render_template('authors.html', authors=authors)

    if request.method == 'POST':
        form = request.form
        if form["target"] == 'delete':
            if Author.delete_author_by_id(form["id"]):
                authors = Author.get_all_authors()
                if(authors):
                    return render_template('authors.html', authors=authors)

        if request.form["target"] == 'update':
            

    return render_template('index.html')


if __name__ == '__main__':
    database.createDB()

    # books = [Book(None, "12319123", "Adventure", "Lady Midnight", "2020-03-13"),
    #          Book(None, "12314222", "Adventure", "Lord of Shadows", "2018-03-13"),
    #          Book(None, "54569123", "Info", "How to program", "2016-03-09"),
    #          Book(None, "12319123", "Info", "Giving you them", "2021-05-13")]

    # for book in books:
    #     book.add_book()

    # authors = [Author(None, "David"),
    #           Author(None, "Arthur"),
    #           Author(None, "Mikey"),
    #           Author(None, "JTT")]

    # for author in authors:
    #     author.add_author()

    app.run(debug=True)
