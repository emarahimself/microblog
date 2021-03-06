from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Mohamed'
    }
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for user: {form.username.data}')
        return redirect(url_for('index'))

    return render_template('login.html', form=form, title='Sign In')
