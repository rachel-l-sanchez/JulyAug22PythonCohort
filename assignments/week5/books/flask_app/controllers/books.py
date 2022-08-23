from flask_app import app
from flask_app.models import book, author
from flask import Flask, render_template,request, redirect, session

@app.route('/books')
def books():
    return render_template('book.html', all_books = book.Book.all_books())

@app.route('/create/book', methods=["POST"])
def createBook():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    book.Book.create_book(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def viewBooks(id):
    data = {
        "id": id
    }
    return render_template('bookShow.html', sel_books = book.Book.join_all(data), all_authors = author.Author.all_authors(), one_book= book.Book.get_one(data))

@app.route('/book/join', methods= ["POST"])
def joinBooks():
    data = {
        'authors_id': request.form['authors_id'],
        'books_id': request.form['books_id']
    }
    book.Book.add_favorite(data)
    return redirect('/books')