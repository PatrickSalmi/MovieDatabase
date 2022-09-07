from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    categories = ["Movies", "Actors", "Directors"]
    return render_template("index.html", message="Tervetuloa!", items=categories)

@app.route("/page/<int:id>")
def page(id):
    return "Tämä on sivu " + str(id)