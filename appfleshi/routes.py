from flask import render_template
from appfleshi import app, login_manager
from flask_login import login_required
from appfleshi.forms import LoginForm, RegisterForm

from appfleshi import app

@app.route('/')
def homepage():
    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)

@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    register_form = RegisterForm()
    return render_template('createaccount.html', form=register_form)

@app.route('/profile/<username>')
@login_manager.user_loader
def profile(username):
    return render_template('profile.html', username=username)