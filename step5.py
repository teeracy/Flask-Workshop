from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to the homepage!"

@app.route("/hello/")
def hello():
    return "Hello recurser!"

@app.route('/hello/<name>')
def helloPerson(name):
    return render_template('helloPerson5.html')

if __name__ == "__main__":
    app.debug = True
    app.run()