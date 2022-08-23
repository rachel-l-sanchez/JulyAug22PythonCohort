from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask import Flask, session
from pprint import pprint

class Author:
    DB = 'booksschema'
    
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
       
        self.on_books = []
    
    @classmethod
    def create_author(cls,data):
        query = """
        INSERT into authors (name, created_at, updated_at)
        values(%(name)s, NOW(), NOW())
        ;"""
        authors_id = connectToMySQL(cls.DB).query_db(query, data)
        session['authors_id'] = authors_id
        return True

    @classmethod
    def all_authors(cls):
        query = " SELECT * FROM authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for a in results:
            authors.append(cls(a))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = """
        INSERT into favorites (authors.id, books_id)
        values (%(authors.id)s,%(books_id)s)
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def join_all(cls, data):
        query = """
        SELECT * FROM authors
        LEFT JOIN favorites on authors.id = favorites.authors_id
        LEFT JOIN books on books.id = favorites.books_id
        WHERE authors.id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        author = cls(results[0])
        for row in results:
            #if there are no favorited books currently
            if row['books.id'] == None:
                break
            #add data table model, info you want stored
            data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            #append into empty list created in init
            author.on_books.append(book.Book(data))
        return author   

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from authors where authors.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    

