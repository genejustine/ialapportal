from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!!!"

@app.route("/gene")
def gene():
    return "Hello Gene Justine :)"

@app.route("/<string:name>")
def visitor(name):
    name = name.capitalize()
    return f"<h1>Welcome, {name}! </h1>"