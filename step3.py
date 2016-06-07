from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to the homepage!"

@app.route("/hello/")
def hello():
    return "Hello recurser!"

if __name__ == "__main__":
    app.debug = True
    app.run()