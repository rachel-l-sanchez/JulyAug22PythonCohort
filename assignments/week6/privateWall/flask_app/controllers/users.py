from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_app.models import user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/user', methods=['POST'])
def register():
    if user.User.save(request.form):
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if user.User.login_user(request.form):
        return redirect('/dashboard')
    return redirect('/')


@app.route('/logout/user')
def logout():
    session.clear()
    return redirect('/')
