from app import app
import users
import movies
from flask import render_template, request, redirect, session

@app.route("/")
def index():
    list = movies.movie_list()
    return render_template("index.html", list=list)

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="wrong username or password")
        return redirect("/")

@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 15:
            return render_template("error.html", message="username too long or short")
        password = request.form["password"]
        password2 = request.form["password2"]
        if password != password2 or len(password) < 6:
            return render_template("error.html", message="Passwords do not match or too short")
        users.register(username, password)
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/add_movie",methods=["GET", "POST"])
def add_movie():
    genres = movies.genres()
    if request.method == "GET":
        return render_template("add_movie.html", genres = genres)
    if request.method == "POST":
        name = request.form["name"]
        release = request.form["release"]
        director = request.form["director"]
        genre = request.form["genre"]
        movies.add_movie(name, release, director, genre)
        return redirect("/")

@app.route("/movie/<name>",methods=["GET", "POST"])
def movie(name):
    movie_info = movies.movie(name)
    if request.method == "GET":
        return render_template("movie.html",
                            id = movie_info[0],
                            name = movie_info[1],
                            release = movie_info[2],
                            director = movie_info[3],
                            genre = movie_info[4])
    if request.method == "POST":
        movies.add_watchlist(movie_info[0])
        return redirect("/watchlist")

@app.route("/watchlist")
def watchlist():
    list = movies.watchlist()
    return render_template("watchlist.html", list=list)

@app.route("/review/<name>",methods=["GET", "POST"])
def review(name):
    if request.method =="GET":
        return render_template("review.html")
    if request.method == "POST":
        movie_info = movies.movie(name)
        stars = request.form["stars"]
        if stars < 0 or stars > 10:
            return render_template("error.html", message="Rating must be between 0-10")
        comment = request.form["comment"]
        movies.reviews(movie_info[0], stars, comment)
        return redirect("/")
