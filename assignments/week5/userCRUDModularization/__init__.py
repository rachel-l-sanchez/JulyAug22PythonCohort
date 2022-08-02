from flask import Flask, render_template, redirect,request, session, flash
app=Flask(__name__,template_folder='templates')
app.secret_key = 'keep it secret, keep it safe'
