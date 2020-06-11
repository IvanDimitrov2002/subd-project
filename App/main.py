from flask import Flask
from flask import render_template
from flask import url_for
import database.create as database

from models.books import Book

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
    app.run(debug=True)
