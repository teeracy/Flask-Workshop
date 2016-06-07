from flask import Flask
from flask import render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to the homepage!"

@app.route("/hello/")
def hello():
    return "Hello recurser!"

@app.route('/hello/<name>/')
def helloPerson(name):
    return render_template('helloPerson7.html', 
    	message=None,
    	name=name,
    )

@app.route('/hello/<name>/', methods=['POST'])
def confirmName(name):
	print request.values.get('name')
	enteredName = request.values.get('name')
	if name == enteredName:
		return redirect('/hello/')
	else:
		return render_template('helloPerson9.html', 
    	message="That's not you! Try again!",
    	name=name,
    )

if __name__ == "__main__":
    app.debug = True
    app.run()