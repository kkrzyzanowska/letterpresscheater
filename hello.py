import os
from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello():
    return 'Hello world!'
