from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to the homepage!"

@app.route("/hello/")
def hello():
    return "Hello recurser!"

@app.route('/hello/<name>')
def helloPerson(name):
    return "Hello there, %s" % name

if __name__ == "__main__":
    app.debug = True
    app.run()