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
    app.run(debug=True)
