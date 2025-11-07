from flask import Flask
from flask import render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
import db
import config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/logout")
def logout():
    del session["user"]
    del session["id"]
    return redirect("/")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if password1 != password2:
        return render_template("signin.html", message="Salasanat eivät täsmää!")

    else:
        phash = generate_password_hash(password1) 
        db.exec("INSERT INTO users (username, password) VALUES (?, ?)", [username, phash])
        return render_template("index.html", message="Käyttäjätunnus luotu, ole hyvä ja kirjaudu sisään.")

@app.route("/verify", methods=["POST"])
def verify():
    username = request.form["username"]
    password = request.form["password"]

    res = db.query("SELECT id, password FROM users WHERE username = ?", [username])
    if res and check_password_hash(res[0]['password'], password):
        session['user'] = username
        session['id'] = res[0]['id']
        return redirect("/")
    else:
        return render_template("signin.html", message="Virheelliset käyttäjätunnukset!")



    