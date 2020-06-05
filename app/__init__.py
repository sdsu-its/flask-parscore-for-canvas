from flask import Flask
app = Flask(__name__)
from flask import Flask, render_template ,redirect
from flask_socketio import SocketIO
from app.config import Config

#init statements
socketio = SocketIO(app)
app.config.from_object(Config)
from app import routes