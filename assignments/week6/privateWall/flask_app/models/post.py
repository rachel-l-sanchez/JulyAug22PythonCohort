from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, session, flash
from flask_bcrypt import Bcrypt
app=Flask(__name__,template_folder='templates')
from flask_app.models import user
bcrypt = Bcrypt(app)
import re

class Post:
    DB = 'wallDB'

    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None
    
    @classmethod
    def createPost(cls,data):
        query = """
        INSERT INTO posts (content, user_id, created_at, updated_at)
        VALUES (%(content)s, %(user_id)s,NOW(), NOW())
        ;"""
        post_id = connectToMySQL(cls.DB).query_db(query, data)
        session['post_id'] = post_id
        return True
    
    @staticmethod
    def validatePost(post):
        is_valid = True
        if post['content'] == "":
            flash("Content must not be blank")
            is_valid = False
        return is_valid
    
    @classmethod
    def deletePost(cls, data):
        query = "DELETE from posts where id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(cls, data)

    @classmethod
    def select_all(cls):
        query = "SELECT * from posts;"
        results_from_db = connectToMySQL(cls.DB).query_db(query)
        posts = []
        for post in results_from_db:
            posts.append(cls(post))
        return posts
    
    @classmethod
    def join_all(cls):
        query = """
        SELECT * FROM posts
        LEFT JOIN users on posts.user_id = users.id
        ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        allPosts = []
        for row in results:
            onePost = cls(row)
            print("onePost", onePost)
            one_post_user_info = {
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                'updated_at': row['updated_at']
            }
            users = user.User(one_post_user_info)
            onePost.creator = users
            allPosts.append(onePost)
        return allPosts