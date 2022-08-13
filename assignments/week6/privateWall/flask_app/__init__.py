from flask import Flask, render_template, redirect,request, session, flash
app=Flask(__name__,template_folder='templates')
app.secret_key = "the first rule of secret key is that we don't talk about secret key"
