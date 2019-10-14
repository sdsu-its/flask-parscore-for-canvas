#imports
from app import app
if __name__ == '__main__':
    app.run()


# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')
# #example of a socketio event
# #called from javascript with .emit
# @socketio.on('my event')
# def handle_my_custom_event(jsona, methods=['GET', 'POST']):
#     print('received my event: ' + str(jsona))
#     socketio.emit('user authenticated',callback=messageReceived())
#
#
# if __name__ == '__main__':
#     socketio.run(app, host="0.0.0.0", port=80,debug=False)
