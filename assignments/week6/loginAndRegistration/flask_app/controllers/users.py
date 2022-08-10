from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.form['password'] and request.form['conf_password'] != "":
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        password_hash= bcrypt.generate_password_hash(request.form['conf_password'])
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash,
            'conf_password': password_hash
        }
        user_id = user.User.save(data)
        session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    users = user.User.login_by_email()
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    user_in_db = user.User.login_by_email(data)
    if not user_in_db:
        flash('Email and/or password combination are incorrect')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Email and/or password combination are incorrect')
        return redirect('/')
    session['user_id'] = user_in_db.id

    return redirect('/dashboard')

@app.route('/dashboard')
def logout():
    if 'user_id' not in session:
        return redirect('/logout/user')
    data = {
        'id': session['user_id']
    }
    return render_template('logout.html', users=user.User.select_all(data) )

@app.route('/dashboard/user', methods=['POST'])
def userDash():
    session['first_name'] = request.form['first_name']
    user_in_db = request.form.get['first_name']
    return redirect('/dashboard')

@app.route('/logout/user')
def logout_user():
    session.clear()
    return redirect('/')