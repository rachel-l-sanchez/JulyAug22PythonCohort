from flask_app.controllers import books, authors
from flask_app import app
from flask import Flask, render_template,request, redirect, session

if __name__ =="__main__":
    app.run(debug=True, port = 5001)