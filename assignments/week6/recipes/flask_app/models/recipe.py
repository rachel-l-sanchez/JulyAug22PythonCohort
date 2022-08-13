from flask import Flask, session, flash
from flask_bcrypt import Bcrypt
app=Flask(__name__,template_folder='templates')
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
import re

class Recipe:
    DB = "recipesDB"
    
    def __init__(self, data):
        self.id= data['id']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.users_id = data['users_id']
        self.description = data['description']
        self.time = data['time']
        self.name = data['name']
        self.creator = None

    @classmethod    
    def save(cls, data):
        query = """
        INSERT INTO recipes (instructions, date_made, description, time, name, users_id)
        values (%(instructions)s, %(date_made)s, %(description)s, %(time)s, %(name)s, %(users_id)s)
        ;"""
        recipe_id = connectToMySQL(cls.DB).query_db(query, data) 
        session['recipe_id'] = recipe_id
        session['description'] = f"{data['description']}"
        session['time'] = f"{data['time']}"
        session['instructions'] = f"{data['instructions']}"
        session['date_made'] = f"{data['date_made']}"
        session['name'] = f"{data['name']}"
        return True
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if recipe['name'] == "":
            flash("Name must not be blank")
            is_valid = False
        if recipe['description'] == "":
            flash("description must not be blank")
            is_valid = False
        if recipe['instructions'] == "":
            flash("Instructions must not be blank")
            is_valid = False
        if len([recipe['name']]) <3:
            flash("Invalid entry. Fields require more characters")
            is_valid = False
        if len(recipe['description']) <3:
            flash("Invalid entry. Fields require more characters")
            is_valid = False
        if len(recipe['instructions']) <3:
            flash("Invalid entry. Fields require more characters")
            is_valid = False
        if recipe['date_made'] == "":
            flash("Date cooked must not be blank")
            is_valid = False
        if recipe['time'] == "":
            flash("Time must not be blank")
            is_valid = False
        return is_valid

    @classmethod
    def edit(cls, data):
        query = """
        UPDATE recipes
        SET instructions =%(instructions)s ,date_made = %(date_made)s, description=%(description)s, name = %(name)s,time = %(time)s
        where recipes.id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def deleteRecipe(cls, data):
        query = "DELETE from recipes where recipes.id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(cls, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * from recipes where id= %(id)s;"
        results = connectToMySQL(cls.DB).query_db(cls, data)
        return results
    
    @classmethod
    def allRecipes(cls):
        query = "SELECT * from recipes;"
        return connectToMySQL(cls.DB).query_db(cls)

    @classmethod
    def join_all(cls):
        query = """SELECT * FROM recipes
        LEFT JOIN users on recipes.users_id = users.id
        ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_recipes = []
        for row in results:
            one_recipe = cls(row)
            print("one_recipe", one_recipe)
            one_recipe_user_info = {
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "conf_password": row['conf_password']
            }
            users = user.User(one_recipe_user_info)
            one_recipe.creator = users
            all_recipes.append(one_recipe)
        return all_recipes
