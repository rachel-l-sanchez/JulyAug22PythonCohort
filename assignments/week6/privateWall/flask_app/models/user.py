from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, session, flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
import re

class User:
    DB = 'wallDB'

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []

    #ensures user is validated before registering
    # ensures password is hashed before saving
    # store user info and the user name in session   
    @classmethod    
    def save(cls, data):
        if not cls.validate_register(data):
            return False
        data = cls.parse_registration(data)
        query = """
        INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s, NOW(), NOW())
        ;"""
        user_id = connectToMySQL(cls.DB).query_db(query, data)
        session['user_id'] = user_id
        session['first_name'] = f"{data['first_name']}"
        print("session key", session['user_id'])
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
        if user['password'] != user['confirm_password']:
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
    
        