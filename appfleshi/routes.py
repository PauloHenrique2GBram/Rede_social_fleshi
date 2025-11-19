from flask import render_template
from appfleshi import app, login_manager
from flask_login import login_required

from appfleshi import app

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile/<username>')
@login_manager.user_loader
def profile(username):
    return render_template('profile.html', username=username)
