from unittest import result
from db import db
from flask import request, session
import users

def add_movie(name: str, release: int, director: str, genre: str):
    sql = "INSERT INTO movies (name, release, director, genre) VALUES (:name, :release, :director, :genre)"
    db.session.execute(sql, {"name":name, "release":release, "director":director, "genre":genre})
    db.session.commit()

def movie(name):
    sql = "SELECT id, name, release, director, genre FROM movies WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    return result.fetchone()

def genres():
    sql = "SELECT name FROM genres"
    result = db.session.execute(sql)
    return result.fetchall()

def movie_list():
    sql = "SELECT name FROM movies"
    result = db.session.execute(sql)
    return result.fetchall()

def watchlist():
    sql = "SELECT M.name FROM movies M, users U, watchlists W WHERE M.id = W.movie_id AND U.id = user_id"
    result = db.session.execute(sql)
    return result.fetchall()

def add_watchlist(movieid):
    userid = users.user_id()
    sql = "INSERT INTO watchlists (user_id, movie_id) VALUES (:user_id, :movie_id)"
    db.session.execute(sql, {"user_id":userid, "movie_id":movieid})
    db.session.commit()