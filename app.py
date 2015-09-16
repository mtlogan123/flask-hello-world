#----Flask Hello World -----#

# import the Flask class from the flask module
from flask import Flask

# create the applications object
app = Flask(__name__)

# error handling
app.config["DEBUG"]= True

# use decorators to link the function to an url
@app.route("/")
@app.route("/hello")
#@app.route("/test/<search_query>")
#@app.route("/path/<path:value>")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, Troy's world!?!?!?! haro yes"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

#def int_type(value):
#	print value
#	return "correct"


# start the development server using the run() method
if __name__ =="__main__":
	app.run()