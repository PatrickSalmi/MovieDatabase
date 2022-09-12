from app import app
import users
from flask import render_template, request, redirect, session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"] 
        if not users.login(username, password):
            return render_template("error.html")
        return redirect("/")

@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.register(username, password)
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
