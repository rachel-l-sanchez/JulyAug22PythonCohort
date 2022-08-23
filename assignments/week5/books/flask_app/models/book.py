from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask import Flask, session
from pprint import pp 

class Book:
    DB = 'booksschema'
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_books = []
    
    @classmethod
    def create_book(cls,data):
        query = """
        INSERT into books (title, num_of_pages, created_at, updated_at)
        values(%(title)s, %(num_of_pages)s,NOW(), NOW())
        ;"""
        books_id =  connectToMySQL(cls.DB).query_db(query, data)
        session['books_id'] = books_id
        session['title'] = f"{data['title']}"
        return True

    @classmethod
    def all_books(cls):
        query = " SELECT * FROM books;"
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for b in results:
            books.append(cls(b))
        return books

    @classmethod
    def join_all(cls, data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites on books.id = favorites.books_id
        LEFT JOIN authors ON authors.id = favorites.authors_id
        WHERE books.id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        books = cls(results[0])
        pp(books, depth=2)
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                'id': row['authors.id'],
                'name': row['name']
            }
            books.favorited_books.append(author.Author(data))
            pp(books)
        return books
    
    
    @classmethod
    def add_favorite(cls,data):
        query = """
        INSERT into favorites (authors.id, books.id)
        values (%(authors.id)s,%(books_id)s)
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
     
    @classmethod
    def get_one(cls, data):
        query = "SELECT * from books where books.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    


    

        