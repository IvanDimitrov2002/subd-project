from flask import Flask, render_template, url_for, request
import database.create as database
from models.book import Book

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/books', methods=['GET', 'POST', 'DELETE'])
def view_books():
    if request.method == 'GET':
        books = []
        search_result = request.args.get('title')
        books = Book.find_by_substring(search_result)
        if(books is None):
            books = Book.get_all_books()
        if(books is None):
            return render_template('index.html')
        return render_template('books.html', books=books)
    if request.method == 'POST' and request.form["target"] == 'delete':
        if Book.delete_book_by_id(request.form["id"]):
            books = Book.get_all_books()
            if(books is None):
                return render_template('index.html')
            return render_template('books.html', books=books)


if __name__ == '__main__':
    database.createDB()

    # books = [Book(None, "12319123", "Adventure", "Lady Midnight", "2020-03-13"),
    #          Book(None, "12314222", "Adventure", "Lord of Shadows", "2018-03-13"),
    #          Book(None, "54569123", "Info", "How to program", "2016-03-09"),
    #          Book(None, "12319123", "Info", "Giving you them", "2021-05-13")]

    # for book in books:
    #     book.add_book()

    app.run(debug=True)
