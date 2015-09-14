#----Flask Hello World -----#

# import the Flask class from the flask module
from flask import Flask

# create the applications object
app = Flask(__name__)

# use decorators to link the function to an url
#@app.route("/")
#@app.route("/hello")
#@app.route("/test/<search_query>")
@app.route("/integer/<int:value>")
def int_type(value):
	print value +1
	return "correct"
@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"
def search(search_query):
	return search_query

# define the view using a function, which returns a string
def hello_world():
	return "Hello, Troy's world!"

# start the development server using the run() method
if __name__ =="__main__":
	app.run()