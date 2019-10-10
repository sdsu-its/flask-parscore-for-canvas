from flask import Flask
app = Flask(__name__)
from app import routes
from flask import Flask, render_template , flash ,redirect
from app.forms import LoginForm
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
#init statements


socketio = SocketIO(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)