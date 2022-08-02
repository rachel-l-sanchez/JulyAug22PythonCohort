from models.user import User
from flask import render_template,request, redirect, session, flash
from __init__ import app

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create/user', methods = ['POST'])
def create_user():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email']
    }
    User.save(data)
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template('read.html', user=user)

@app.route('/delete/user/<int:id>', methods = ['POST'])
def delete_user_by_id():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': request.form['id']
    }
    user = User.delete(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def update(id):
    data = {
        'id': id
    }
    user = User.get_one(data)
    return render_template('update.html', user=user)
    
@app.route('/update/<int:id>', methods=['POST'])
def upd_user():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': request.form['id']
    }
    user = User.update(data)
    return redirect('/')
           
    
    