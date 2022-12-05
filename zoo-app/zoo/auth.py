from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt, model

import flask_login

bp = Blueprint("auth", __name__)

@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")

@bp.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    print(email, flush=True)
    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("The passwords you have entered are different.")
        return redirect(url_for("auth.signup"))
    # Check if the email is already at the database
    user = model.User.query.filter_by(email=email).first()
    if user:
        flash("Sorry, the email you provided is already registered.")
        return redirect(url_for("auth.signup"))
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(email=email, username=username, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login"))

@bp.route("/login")
def login():
    return render_template("auth/signin.html")

@bp.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    # Get the user with that email from the database:
    user = model.User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # The user exists and the password is correct
        flask_login.login_user(user)
        return redirect(url_for("main.index_logged_in", name=user.username))
    else:
        flash("This email and password does not match our records")
        return redirect(url_for("auth.login"))

@bp.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("main.index"))
