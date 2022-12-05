import flask_login

from flask import Blueprint, render_template, request, redirect, url_for, flash

from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("main/index.html")

@bp.route("/logged_in")
@flask_login.login_required
def index_logged_in():
    return render_template("main/index_logged_in.html")

@bp.route("/animals")
def animals():
    animals = model.Animal.query.all()

    return render_template("main/animals.html", animals=animals)

@bp.route("/faq")
def faq():
    faq_items = model.Faq.query.all()
    return render_template("main/faq.html", faq_items=faq_items)