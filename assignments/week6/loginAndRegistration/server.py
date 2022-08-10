from flask_app.controllers import users
from flask_app import app
from flask import Flask, render_template,request, redirect, session, flash

if __name__ =="__main__":
    app.run(debug=True, port = 5001)