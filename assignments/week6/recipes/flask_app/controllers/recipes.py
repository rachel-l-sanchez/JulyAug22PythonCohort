from flask import Flask, render_template, redirect,request, session
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import user, recipe

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create/recipe', methods=['POST'])
def createRecipe():
    if 'user_id' not in session:
        if not recipe.Recipe.validate_recipe(request.form):
            return redirect('/')
    data = {
            "instructions" : request.form['instructions'],
            "date_made": request.form['date_made'],
            "description": request.form['description'],
            "time": request.form['time'],
            "name": request.form['name'],
            "users_id": session['user_id']
        }
    recipe.Recipe.save(data)
    return redirect('/view')
      
@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    oneRecipe = recipe.Recipe.get_one(data)
    return render_template('edit.html', oneRecipe = oneRecipe)

@app.route('/edit/recipe', methods=['POST'])
def editRecipe():   
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/view')
    data = {
        "instructions" : request.form['instructions'],
        "date_made" : request.form['date_made'],
        "description" : request.form['description'],
        "time" : request.form['time'],
        "name" : request.form['name']
    }
    recipe.Recipe.edit(data)
    return redirect('/view')    
    

@app.route('/recipe/<int:id>')
def viewRecipe(id):
    data = {
        'id': id
    }
    return render_template('recipe.html', recipes = recipe.Recipe.get_one(data))


@app.route('/delete/recipe/<int:id>', methods = ['POST'])
def deleteRecipe(id):
    data = {
        'id': request.form['recipes.id']
    }
    recipe.Recipe.deleteRecipe(data)
    return redirect('/view')