<<<<<<< HEAD
=======
#imports
from app import app
if __name__ == '__main__':
    app.run()
>>>>>>> 65cbe3f625be42f137baefe99a65f034634ce27c

# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

