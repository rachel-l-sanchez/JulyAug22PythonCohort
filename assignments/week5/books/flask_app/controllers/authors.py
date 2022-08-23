from flask_app import app
from flask_app.models import book, author
from flask import Flask, render_template,request, redirect, session

@app.route('/')
def index():
    return render_template('authors.html', all_authors = author.Author.all_authors())

@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    author.Author.create_author(data)
    return redirect('/')

@app.route('/author/<int:id>')
def authors(id):
    data = {
       'id':id
    }
    return render_template('authorShow.html', allAuthor = author.Author.join_all(data), allBooks = book.Book.all_books(), book = book.Book.get_one(data), oneAuthor = author.Author.get_one(data))

@app.route('/add/favorite', methods = ['POST'])
def join():
    data = {
        'books_id': request.form['books_id'],
        'authors_id': request.form['authors_id']
    }
    author.Author.add_favorite(data)
    return redirect('/')