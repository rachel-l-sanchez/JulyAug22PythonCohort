from flask import Flask, render_template, redirect,request, session, flash
from flask_bcrypt import Bcrypt
app=Flask(__name__,template_folder='templates')
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'login'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password= data['password']
        self.conf_password= data['conf_password']

    @classmethod    
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password, conf_password)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s, %(conf_password)s)
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters long")
            is_valid = False
        if len(user['last_name'])< 2:
            flash("Last Name must be at least 2 characters long")
            is_valid = False
        if len(user['email']):
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters long")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if (user['password']) != (user['conf_password']):
            flash("Password does not match")
            is_valid = False
        if (user['password'].isalpha()) == True:
            flash("Password must contain at least one number")
            is_valid = False
        if (user['password'].islower()) == True:
            flash("Password must contain one uppercase characters")
            is_valid = False
        return is_valid
    
    @classmethod
    def login_by_email(cls, data):
        query = "SELECT * from users where email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])
    
    @classmethod
    def select_name(cls, data):
        query = "SELECT first_name from users where id=%(id)s;"
        results =  connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def select_all(cls, data):
        query = "SELECT * from users where id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query)
        return results