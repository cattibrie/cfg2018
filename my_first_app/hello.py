from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hi Kate!"

@app.route("/iexistnow")
def exist():
    return "Hello again!"

@app.route("/wednesday")
def wednesday():
    return "It's Wednesday!"

app.run(debug=True)
