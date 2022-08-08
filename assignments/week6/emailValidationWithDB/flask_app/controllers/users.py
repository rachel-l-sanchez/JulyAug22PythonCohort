from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_app.models import user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_login(request.form):
        flash("Info is not valid. Fields cannot be blank and email must be in proper format")
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user.User.save(request.form)
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def dashboard():
    data = {
        'id': id
    }
    allUsers = user.User.select_all()
    print(allUsers)
    
    return render_template('userDash.html', allUsers = allUsers)

@app.route('/edit/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    return render_template('update.html', users = user.User.get_one(data))

@app.route('/edit/user', methods=['POST'])
def update_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    users = user.User.update(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    return render_template('userDash.html', users = user.User.get_one(data))

@app.route('/delete/user/<int:id>', methods=['POST'])
def delete_user():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': request.form['id']
    }
    user.User.delete(data)