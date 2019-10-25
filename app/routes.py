from app import app
from flask import Flask, render_template , flash ,redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User, Course, Major, Admin, Student, Teacher
from flask_login import logout_user
from flask_login import login_required
#Routes
#---Each function represents a different page given by the app.route argument
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/Users')
def Users():
    UserList=User.query.all()
    TeacherList=User.query.filter(User.access_level=='Teacher').all()
    AdminList=User.query.filter(User.access_level=='Admin').all()
    StudentList=User.query.filter(User.access_level=='Student').all()
    return render_template('Users.html',title='Users',UserList=UserList,AdminList=AdminList,StudentList=StudentList,TeacherList=TeacherList)
@app.route('/classes')
def classes():
    current_courses =Course.query.all()
    return render_template('classes.html',title='Classes',course_list=current_courses)
@app.route('/majors')
def majors():
    current_majors = Major.query.all()
    return render_template('majors.html',title='Majors',major_list=current_majors)
@app.route('/')
@app.route('/index')
@login_required
def index():
    print("going to home screen")
    return render_template('index.html')

from app import db
from app.forms import RegistrationForm

# ...
@login_required
@app.route('/register', methods=['GET', 'POST'])
def register():
    if not current_user.access_level == 'Admin':
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User()
        print('the radio button said')
        print(form.access_level.data)
        if(form.access_level.data=='student'):
            user = Student(username=form.username.data, email=form.email.data)
        if(form.access_level.data=='system'):
            user = Admin(username=form.username.data, email=form.email.data)
        if(form.access_level.data=='teacher'):
            user = Teacher(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have registered a new User')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)