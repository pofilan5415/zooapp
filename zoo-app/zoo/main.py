import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(email="mary@example.com", username="mary")
    return render_template("main/index.html")

@bp.route("/animals")
def animals():
    """
    polar_bear = model.Animal(1, "Polar Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/qQWV91TTBrE")
    brown_bear = model.Animal(2, "Brown Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/y421kXlUOQk")
    tiger = model.Animal(3, "Tiger", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/opnyo_F5l3o")
    snake = model.Animal(4, "Snake", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/o1bdnLXC5NM")
    toucan = model.Animal(5, "Toucan", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/cfIcTiopin4")
    shark = model.Animal(6, "Shark", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/GBDkr3k96DE")
    """
    animals = model.Animal.query.all()

    return render_template("main/animals.html", animals=animals)

@bp.route("/faq")
def faq():
    """
    item1 = model.FaqItem(1, "Are pets allowed at the park?", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.")
    item2 = model.FaqItem(2, "What are the hours of the park?", "Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.")
    item3 = model.FaqItem(3, "Can we pet any of the animals?", "If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur.")
    item4 = model.FaqItem(4, "Does the zoo include an aquarium?", "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.")
    """
    faq_items = model.Faq.query.all()

    return render_template("main/faq.html", faq_items=faq_items)