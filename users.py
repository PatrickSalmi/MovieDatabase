from db import db
from flask import request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        pass
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username

def register(username, password):
    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def logout():
    del session["username"]