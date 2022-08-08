from flask import Flask,redirect, session, request, flash
app=Flask(__name__,template_folder='templates')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'emailvalid'
    
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.created_at=data['created_at']
    
    @classmethod    
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, created_at)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, NOW())
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    # ensure login information conforms to allowed security specifications
    @staticmethod
    def validate_login(user):
        is_valid = True
        ACCOUNT_UNIQUE_EMAIL = True
        if len(user['first_name']) == 0:
            flash("First Name cannot be blank")
            is_valid = False
        if len(user['last_name']) ==0:
            flash("Last Name cannot be blank")
            is_valid = False
        if len(user['email']) ==0:
            flash("Email cannot be blank")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['email'].count(user['email']) > 1:
            flash('Invalid email address. Please choose unique value')
            is_valid = False
        return is_valid
    
    @classmethod
    def update(cls,data):
        query = """
        UPDATE users 
        SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, created_at= NOW()
        where id=%(id)s);"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE from users where id=%(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = " SELECT * from users where id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def select_all(cls):
        query = "SELECT * from users;"
        return connectToMySQL(cls.DB).query_db(query)    

    