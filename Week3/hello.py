from flask import Flask, render_template, request
import re
import json
from flask_moment import Moment

f = open("users.json")
users = json.load(f)

app = Flask(__name__)

moment = Moment(app)

@app.route("/")
def index(): 
    return render_template("index.html")

# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html", name=name)

@app.route("/user/<email>")
def get_user(email):
    pattern = re.compile("^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,4}$")
    if (pattern.match(email)):
        for u in users:
            if (u["email"]==email):
                return "Hello <strong>{} {}</strong>".format(u["FIRST_NAME"], u["LAST_NAME"])
    return "<h1>404</h1>", 404

@app.route("/get-user-agent")
def get_user_agent():
    return "Your browser is <strong>{}</strong>".format(request.user_agent)
