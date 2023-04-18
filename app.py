from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/collections')
def collections():
    return render_template('collections.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')
