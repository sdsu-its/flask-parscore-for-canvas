
#imports
from app import app, db
from app.models import User, Admin, Teacher, Major, Student, Course

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Course': Course, 'Teacher':Teacher,'Student':Student,'Major':Major,'Admin':Admin}
if __name__ == '__main__':
    app.run()


