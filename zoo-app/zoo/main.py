import datetime
import dateutil.tz

from flask import Blueprint, render_template, request


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
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/animals")
def animals():
    polar_bear = model.Animal(1, "Polar Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/qQWV91TTBrE")
    brown_bear = model.Animal(2, "Brown Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/y421kXlUOQk")
    tiger = model.Animal(3, "Tiger", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/opnyo_F5l3o")
    snake = model.Animal(4, "Snake", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/o1bdnLXC5NM")
    toucan = model.Animal(5, "Toucan", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/cfIcTiopin4")
    shark = model.Animal(6, "Shark", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/GBDkr3k96DE")

    animals = [polar_bear, brown_bear, tiger, snake, toucan, shark]

    return render_template("main/animals.html", animals=animals)

@bp.route("/faq")
def faq():
    item1 = model.FaqItem(1, "Are pets allowed at the park?", "No, unfortunately pets are not allowed for various saftey reasons.")
    item2 = model.FaqItem(2, "What are the hours of the park?", "The park hours are 9AM - 8PM on weekdays and 8AM - 10PM on weekends.")

    faq_items = [item1, item2]

    return render_template("", faq_items=faq_items)

@bp.route("/animal-info")
def animal_info():
    animal_name = request.args.get('animal', None)

    polar_bear = model.Animal(1, "Polar Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/qQWV91TTBrE")
    brown_bear = model.Animal(2, "Brown Bear", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/y421kXlUOQk")
    tiger = model.Animal(3, "Tiger", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/opnyo_F5l3o")
    snake = model.Animal(4, "Snake", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/o1bdnLXC5NM")
    toucan = model.Animal(5, "Toucan", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/cfIcTiopin4")
    shark = model.Animal(6, "Shark", "Ursus", "A very, very scary animal!", "https://source.unsplash.com/GBDkr3k96DE")

    animals = {
        "Polar Bear": polar_bear,
        "Brown Bear": brown_bear, 
        "Tiger": tiger, 
        "Snake": snake, 
        "Toucan": toucan,
        "Shark": shark
    }

    return render_template("main/animal-info.html", animal=animals[animal_name])