from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'gopi.valleru'}
    posts = [
        {
            'author' : {'username': 'Archana.enturu'},
            'body' : 'Achu dodo'
        },
        {
            'author' : {'username': 'Santha.gutta'},
            'body' : 'Good Morning ' + user['username']
        }
    ]
    return render_template("index.html", title = "Welcome page", user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title = "Log in", loginform = form)