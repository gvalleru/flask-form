from flask import render_template
from app import app

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
