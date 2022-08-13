from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import recipe
from flask_app.config.mysqlconnection import connectToMySQL
import re


class User:
    DB = "recipesDB"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.conf_password = data['conf_password']
        self.recipes = []

    #ensures user is validated before registering
    # ensures password is hashed before saving
    # store user info and the user name in session   
    @classmethod    
    def save(cls, data):
        if not cls.validate_register(data):
            return False
        data = cls.parse_registration(data)
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s)
        ;"""
        user_id = connectToMySQL(cls.DB).query_db(query, data)
        session['user_id'] = user_id
        session['first_name'] = f"{data['first_name']}"
        return True
    
    @classmethod
    def get_user_by_email(cls, email):
        data = { 'email': email}
        query = "SELECT * from users where email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            results = cls(results[0])
            return results
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

        if len(user['first_name']) <3:
            flash('First name invalid')
            is_valid = False
        if len(user['last_name']) <3:
            flash('Invalid last name')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if User.get_user_by_email(user['email'].lower()):
            flash("User already registered")
            is_valid = False
        if user['password'] != user['conf_password']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from users where id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    # prevents the password from being stored in the db without a hash
    @staticmethod
    def parse_registration(data):
        parseData = {}
        parseData['email'] = data['email'].lower()
        parseData['first_name'] = data['first_name']
        parseData['last_name'] = data['last_name']
        parseData['password'] = bcrypt.generate_password_hash(data['password'])
        return parseData
    
    @staticmethod
    def login_user(data):
        current_user= User.get_user_by_email(data['email'])
        if current_user:
            if bcrypt.check_password_hash(current_user.password,data['password']):
                session['user_id'] = current_user.id
                session['first_name'] = f"{current_user.first_name}"
                return True
        flash('Your user information does not match')
        return False
        
    