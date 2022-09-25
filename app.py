from flask import Flask
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("Heroku_SECRET_KEY")

import routes