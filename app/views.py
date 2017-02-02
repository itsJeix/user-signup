from app import app
from flask import Flask, render_template, request, flash, redirect
import cgi
from .forms import LoginForm

movies = ['Videodrome', 'Scanners']

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')

def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return welcome(form.username.data)
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome(username):
    return render_template('welcome.html', user=username)
