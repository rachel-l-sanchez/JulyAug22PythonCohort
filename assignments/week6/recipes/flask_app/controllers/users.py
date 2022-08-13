from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_app.models import user, recipe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/user', methods=['POST'])
def register():
    if user.User.save(request.form):
        return redirect('/view')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if user.User.login_user(request.form):
        return redirect('/view')
    return redirect('/')

@app.route('/view')
def view():
    if 'user_id' not in session:
        return redirect('/')
    recipeData = recipe.Recipe.join_all()
    data = {
        'id': session['user_id']
    }
    users = user.User.get_by_id(data)
    return render_template('view.html', all_recipes = recipeData, users = users)

@app.route('/view/join', methods = ['POST'])
def joinAll():
    one_recipe = recipe.Recipe.join_all()
    return redirect("/view")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
