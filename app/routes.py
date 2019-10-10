from app import app
from flask import Flask, render_template , flash ,redirect
from app.forms import LoginForm
#Routes
#---Each function represents a different page given by the app.route argument
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #notification of login
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def home():
    print("going to home screen")
    return render_template('index.html')
