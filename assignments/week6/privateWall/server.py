from flask_app.controllers import users, posts
from flask_app import app
from flask import Flask, render_template,request, redirect, session

if __name__ =="__main__":
    app.run(debug=True, port = 5002)