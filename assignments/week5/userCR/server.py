from flask import Flask, render_template,request, redirect, session
from controllers.user import User
app=Flask(__name__,template_folder='templates')
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/create/user', methods = ['POST'])
def create_user():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email']
    }
    User.save(data)
    return redirect('/')


if __name__ =="__main__":
    app.run(debug=True, port = 5001)