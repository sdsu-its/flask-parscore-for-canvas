from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    access_level = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return '<User {}>'.format(self.username)
class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_name = db.Column(db.String(128))
    department= db.Column(db.String(128))
    units_required = db.Column(db.Integer)
    required_courses=db.relationship('Course', backref='major_required', lazy='dynamic')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_number = db.Column(db.Integer)
    course_name = db.Column(db.String(128))
    date_and_time = db.Column(db.String(128))
    course_location = db.Column(db.String(128))
    instructor_name = db.Column(db.String(128))
    unit_count = db.Column(db.Integer)
    max_students = db.Column(db.Integer)
    department= db.Column(db.String(128))
    major_id = db.Column(db.Integer, db.ForeignKey('major.id'))
    def __repr__(self):
        return '<Course {}>'.format(self.course_name)


