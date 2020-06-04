from flask import Flask
from flask import render_template
from flask import url_for

import database.create as database


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    database.createDB()
    app.run(debug=True)
