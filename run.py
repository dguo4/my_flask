from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)