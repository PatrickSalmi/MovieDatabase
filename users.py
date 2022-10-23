import secrets
from db import db
from flask import request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
        
    hash_value = user.password
    if check_password_hash(hash_value, password):
        session["user_id"] = user[0]
        session["user_name"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return True
    
    return False

def register(username, password):
    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]
    del session["user_name"]

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)