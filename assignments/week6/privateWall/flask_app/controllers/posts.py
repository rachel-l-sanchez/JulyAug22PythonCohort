from flask import Flask, render_template, redirect,request, session
from flask_app import app
from flask_app.models import user, post

@app.route('/dashboard')
def userDash():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    users = user.User.get_by_id(data)
    return render_template('userDash.html', postData = post.Post.join_all(), users= users)
 
@app.route('/dashboard/join', methods=['POST'])
def joinPosts():
    postData = post.Post.join_all()
    return redirect('/dashboard')

@app.route('/create/post', methods=['POST'])
def createPost():
    if post.Post.validatePost(request.form):
        data = {
            'content': request.form['content'],
            'user_id': session['user_id']
        }
        post.Post.createPost(data)
        return redirect('/dashboard')
    return redirect('/')


@app.route('/delete/post/<int:id>', methods = ['POST'])
def deleteRecipe(id):
    data = {
        'id': request.form['posts.id']
    }
    post.Post.deletePost(data)
    return redirect('/dashboard')
