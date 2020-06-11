from flask import Flask
from flask import render_template
# from flask import url_for

import database.create as database
from models.book import Book

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello World!!!")


@app.route('/books')
def view_all_books(book_name, methods):
    book = Book.find_by_id(id)
    return book


if __name__ == '__main__':
    database.createDB()

    books = [Book("Lady Midnight", "Adventure", "2020-03-13", "12319123"),
             Book("Lord of Shadows", "Adventure", "2018-03-13", "12314222"),
             Book("How to program", "Info", "2016-03-09", "54569123"),
             Book("Giving you them", "Info", "2021-05-13", "12319123")]

    for book in books:
        book.add_book()

    app.run(debug=True)
