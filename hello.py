import os
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello(name=None):
    return render_template('main.html', name=name)


@app.route('/letters/<string:letters>')
def show_results(letters):
    return render_template('show_results.html', letters=letters)
