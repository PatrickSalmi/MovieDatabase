from db import db
from flask import request, session

def add_movie(name: str, release: int, director: str):
    sql = "INSERT INTO movies (name, release, director) VALUES (:name, :release, :director)"
    db.session.execute(sql, {"name":name, "release":release, "director":director})
    db.session.commit()

def movie(name):
    sql = "SELECT id, name, release, director FROM movies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    return result.fetchone()