This repo contains the server side code for The Terminators class project

Getting Started:

	Downloads
	
		This project is written in python 3.7 and utilizes a couple python libraries listed here
		
		get python: https://www.python.org/downloads/
		
		get flask: pip install flask 
		
		get flask-socketio: pip install flask_socketIO
		
	Running the project:
	
		run the script ServerSide.py with 'python ServerSide.py' in the console
		
		go to localhost in any browser to see result
		To see site on a different computer ensure both computers are on the same Wifi (cont)
		
		Search the IPv4 adress of the server computer with ipconfig at the command line
		
		On the client computer go type in that ip into the search bar
		
Documentation:

flask docs: http://flask.palletsprojects.com/en/1.1.x/

python docs: https://docs.python.org/3/

	Basics:
	
		templates:
		
			This code relies on Flask to manager client server communications.
			
			functions with @app.route("") determine what html pages will be loaded when the user requests different url
			
			Ex: a function with @app.route("/home") will be called when then user goes to the url: localhost/home
			
			functions with @app.route("") typically return a call to render_template
			
			render_template takes in arguments for what page should be loaded and what spcific info should be in the page
			
			Ex: 'return render_template('index.html',user=userName)' displays index.html with the variable user
			
			all templates are found in the templates folder
	
		Communication with javascript:
			@socketio.on("event_name") means that a function is an event
			
			events on the ServerSide can be called when the emit function is called in javascript with the correct function name
			
			events in javascript are set with the .on method 
			
			These events can be called from the server side with the .emit function 
			
			All events can have additional arguments passed and recieved as long as the event declaration allows for them
	
	