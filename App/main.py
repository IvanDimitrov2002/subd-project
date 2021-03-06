from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

import database.create as database
from models.book import Book
from models.author import Author

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/books', methods=['GET', 'POST'], endpoint="books")
def view_books():
    books = None
    if request.method == 'GET':
        req = request.args

        if req.get('title') and req.get('title') != "":
            books = Book.find_by_substring(req.get('title'))

        elif req.get('genre') and req.get('genre') != "":
            books = Book.find_by_genre(req.get('genre'))

        elif req.get('author') and req.get('author') != "":
            books = Book.find_by_author(req.get('author'))

    if request.method == 'POST':
        if request.form["target"] == 'delete':
            Book.delete_book_by_id(request.form["id"])

    if not books:
        books = Book.get_all_books()

    if books:
        for book in books:
            authors = book.get_book_authors()
            if(authors):
                book.authors = [author[1] for author in authors]
        return render_template('books.html', books=books)

    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def update_book():
    books = None
    book = None

    if request.method == 'GET':
        book = Book.find_by_id(request.args.get('id'))
        authors = book.get_book_authors()
        if(authors):
            book.authors = ','.join([author[1] for author in authors])
        if book:
            return render_template('update_book.html', book=book)

    if request.method == 'POST':
        form = request.form
        book = Book.find_by_id(form['id'])
        print(form)
        if book:
            book.date = form['date']
            book.genre = form['genre']
            book.isbn = form['isbn']
            book.title = form['title']
            book.authors = [author.strip() for author in
                            request.form['authors'].split(',')]
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

        if req.get('name') and req.get('name') != "":
            authors = Author.find_by_name(req.get('name'))
            return render_template('authors.html', authors=[authors])

        if not authors:
            authors = Author.get_all_authors()
        if authors:
            return render_template('authors.html', authors=authors)

        return render_template('index.html')

    if request.method == 'POST':
        form = request.form
        if form["target"] == 'delete':
            if Author.delete_author_by_id(form["id"]):
                authors = Author.get_all_authors()
                if(authors):
                    return render_template('authors.html', authors=authors)

    return render_template('index.html')


@app.route('/author', methods=['GET', 'POST'])
def update_author():
    authors = None
    author = None
    if request.method == 'GET':
        author = Author.find_by_id(request.args.get('id'))

    if request.method == 'POST':
        form = request.form
        author = Author.find_by_id(form('id'))

        if author:
            author.name = form['name']
            author.update_author()

    if author:
        author.set_author_books()
        return render_template('authors.html', authors=[author])

    authors = Book.get_all_authors()
    if authors:
        for author in authors:
            author.set_author_books()

        return render_template('authors.html', authors=authors)

    return render_template('index.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('add_book.html')

    elif request.method == 'POST':
        authors = [author.strip() for author in request.form['book_authors']
                   .split(',')]
        title = request.form['book_title']
        genre = request.form['book_genre']
        isbn = request.form['book_isbn']
        date = request.form['book_date']
        if authors is not None and title != '' and genre != '' and isbn != '' \
           and date != '':
            book = Book(None, isbn, genre, title, date)
            book.add_book(authors)
            return redirect(url_for('books'))

        elif title == "":
            return render_template('add_book.html', error='Title is reuqered!')

        elif genre == "":
            return render_template('add_book.html', error='Genre is reuqered!')

        elif isbn == "":
            return render_template('add_book.html', error='ISBN is reuqered!')

        elif date == "":
            return render_template('add_book.html', error='Date is reuqered!')

        elif authors is None:
            return render_template('add_book.html', error='''At least one
                                   author is requred!''')


if __name__ == '__main__':
    database.createDB()

    # books = [Book(None, "12319123", "Adventure", "Lady Midnight",
    # "2020-03-13"),
    #          Book(None, "12314222", "Adventure", "Lord of Shadows",
    # "2018-03-13"),
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
