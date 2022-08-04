from flask_app import app
from flask_app.models import ninja, dojo
from flask import Flask, render_template,request, redirect, session, flash

@app.route('/')
def index():
    return render_template("dojo.html", dojos = dojo.Dojo.get_all())

@app.route('/dojo', methods = ['POST'])
def create_dojo():
    data = {
    'dojo_name': request.form['dojo_name']
    }
    dojo.Dojo.create_dojo(data)
    return redirect('/')

@app.route('/ninja')
def create():
    create_dojo = dojo.Dojo.get_all()
   
    return render_template('ninja.html', create_dojo=create_dojo)

@app.route('/ninja/create', methods = ['POST'])
def create_ninjas():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'age': request.form['age'],
    'dojo_id': request.form['dojo_id']
    }
    create_ninja = ninja.Ninja.create_ninja(data)
   
    return redirect('/')


@app.route('/view/ninjas', methods = ['POST'])
def view_ninjas(): 
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_name': request.form['dojo_name'],
        'dojo_id': request.form['dojo_id']
    }
    all_ninjas = ninja.Ninja.view_all(data)
    return redirect('/view')

@app.route('/view/ninjas/<dojo_name>')
def ninja_view(dojo_name):
    data = {
        'dojo_name': dojo_name
    }
    dojo = ninja.Ninja.view_all(data)
    return render_template('view.html', dojo = dojo)



