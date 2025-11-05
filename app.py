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

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:
        return render_template("signin.html", message="Salasanat eivät täsmää!")

    else: #uniikit käyttäjätunnukset
        db.exec("INSERT INTO users (username, password) VALUES (?, ?)", [username, password1])
        return render_template("index.html", message="Käyttäjätunnus luotu, ole hyvä ja kirjaudu sisään.")

@app.route("/verify", methods=["POST"])
def verify():
    username = request.form["username"]
    password = request.form["password"]

    check = db.query("SELECT password FROM users where user (?)", [username])
    
    if not check or check[0] != password:
        return "incorrect credentials"
    else:
        return 'Kirjattu sisään käyttäjänä {username}.'



    