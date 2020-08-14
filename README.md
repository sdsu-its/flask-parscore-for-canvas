This is the repo for a flask web server that provides a conversion from canvas grades to webportal grades

This code is intended to be run on a ubuntu machine with a apache web server. The dependencies include Python3, Flask, pandas, flask-dropzone, and flask-socketio

The front end of the server is located in the app/templates directory

The back end is mostly run from the app/routes.py file

The static resources are in the app/static folder

The site uses Dropzone to accept files from the user and then uses pandasParscoreParser.py to process them and send back the result
