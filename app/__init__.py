from flask import Flask
app = Flask(__name__)
from flask import Flask, render_template , flash ,redirect
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager

#init statements


socketio = SocketIO(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login=LoginManager(app)
login.login_view = 'login'
from app import routes, models