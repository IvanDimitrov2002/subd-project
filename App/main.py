from flask import Flask, render_template, url_for, request
import database.create as database
from models.book import Book

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
def view_books():
    books = []
    search_result = request.args.get('title')
    if(search_result is not None and search_result != ""):
        books = Book.find_by_substring(search_result)
    else:
        books = Book.get_all_books()
    return render_template('books.html', books=books)


if __name__ == '__main__':
    database.createDB()

    books = [Book("Lady Midnight", "Adventure", "2020-03-13", "12319123"),
             Book("Lord of Shadows", "Adventure", "2018-03-13", "12314222"),
             Book("How to program", "Info", "2016-03-09", "54569123"),
             Book("Giving you them", "Info", "2021-05-13", "12319123")]

    for book in books:
        book.add_book()

    app.run(debug=True)
