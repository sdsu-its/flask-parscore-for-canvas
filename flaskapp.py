
#imports
from app import app

#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'User': User, 'Course': Course, 'Teacher':Teacher,'Student':Student,'Major':Major,'Admin':Admin}
import os
from elevate import elevate

if __name__ == '__main__':
    elevatr()	
    app.run()


