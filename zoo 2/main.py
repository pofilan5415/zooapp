import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "mary")
    posts = [
        model.Message(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
              3, user, "third post", datetime.datetime.now(dateutil.tz.tzlocal()))
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(1, "PP@example.com", "PP")
    posts = [
        model.Message(
            1, user, "PP POST", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/profile.html", posts=posts)

@bp.route("/messages")
def message():
    messages = {
        "sup PP": ["hey", "how are you", "great"]
    }
    return render_template("main/messages.html", messages=messages)