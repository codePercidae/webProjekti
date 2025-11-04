from flask import Flask
from flask import render_template, request, redirect
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:
        return "Salasanat eivät täsmää!"

    else:
        db.exec("INSERT INTO users (username, password) VALUES (?, ?)", [username, password1])
        return "Onnistui" 
