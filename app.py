# application.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Welcome to path4cloud trainings !!!</h1>"
