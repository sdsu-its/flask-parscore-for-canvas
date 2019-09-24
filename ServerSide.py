#imports
from flask import Flask, render_template , flash ,redirect , url_for
from app.forms import LoginForm
from flask_socketio import SocketIO
import json
#init statements
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

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

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')
#example of a socketio event
#called from javascript with .emit
@socketio.on('my event')
def handle_my_custom_event(jsona, methods=['GET', 'POST']):
    print('received my event: ' + str(jsona))
    socketio.emit('user authenticated',callback=messageReceived())


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=80,debug=False)