import flask_login
import datetime
import dateutil.tz

from flask import Blueprint, render_template, request

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
    """
    polar_bear = model.Animal(1, "Polar Bear", "Ursus", "Most marine mammals including seals, puffins, and the occasional walrus", "Arctic Circle", "A very, very scary animal!", "https://source.unsplash.com/qQWV91TTBrE")
    brown_bear = model.Animal(2, "Brown Bear", "Ursus", "Salmon, roots, berries", "Brown bears occupy the widest range of habitats of any bear species including dense coastal forests, boreal forests, sub alpine mountain areas, tundra, deciduous forests, and desert and semi-desert areas.", "A very, very scary animal!", "https://source.unsplash.com/y421kXlUOQk")
    tiger = model.Animal(3, "Tiger", "Panthera", "Wild buffalo, deer, boars", "Indian sub-continent", "A very, very scary animal!", "https://source.unsplash.com/opnyo_F5l3o")
    snake = model.Animal(4, "Snake", "Reptilia", "snake diet", "snake habitat", "A very, very scary animal!", "https://source.unsplash.com/o1bdnLXC5NM")
    toucan = model.Animal(5, "Toucan", "Ramphastos", "toucan diet", "toucan habitat", "A very, very scary animal!", "https://source.unsplash.com/cfIcTiopin4")
    shark = model.Animal(6, "Shark", "Carcharodon", "shark diet", "shark habitat", "A very, very scary animal!", "https://source.unsplash.com/GBDkr3k96DE")
    animals = [polar_bear, brown_bear, tiger, snake, toucan, shark]
    """
    return render_template("main/animals.html", animals=animals)

@bp.route("/faq")
def faq():
    faq_items = model.Faq.query.all()
    return render_template("main/faq.html", faq_items=faq_items)
    item1 = model.FaqItem(1, "Are pets allowed at the park?", "No, unfortunately pets are not allowed for various saftey reasons.")
    item2 = model.FaqItem(2, "What are the hours of the park?", "The park hours are 9AM - 8PM on weekdays and 8AM - 10PM on weekends.")

    faq_items = [item1, item2]

    return render_template("", faq_items=faq_items)

@bp.route("/animal-info")
def animal_info():
    animal_id = request.args.get('animal', None)
    animal = model.Animal.query.filter_by(id=animal_id).first()

    return render_template("main/animal-info.html", animal=animal)


@bp.route("/activities")
def activities():
    activities = model.Activity.query.all()
    return render_template("main/activities.html", activities=activities)

@bp.route("/activity-info")
def activity_info():
    activity_id = request.args.get('activity', None)
    activity = model.Activity.query.filter_by(id=activity_id).first()

    

    return render_template("main/activity-info.html", activity=activity)

@bp.route("/schedule")
def schedule():

    activity_name = request.args.get('activity', None)
    t = request.args.get('t', None)
    

    print("________________", flush=True)
    print("NAME: ", activity_name, flush=True)
    print("TIME: ", t, flush=True)
    print("________________", flush=True)

    act1 = model.Activity("Jungle Cruise", "Join us on a cruise through the great jungles of Spain and see all the scary animals. ", "https://source.unsplash.com/SFkv16V_09c", t)
    act2 = model.Activity("Guided Wilderness Hike", "We will take you on a guided hike to see all the scary animals.", "https://source.unsplash.com/3WJiY5vBLT0", t)
    act3 = model.Activity("Petting Park", "Pet all the scary animals.", "https://source.unsplash.com/o11YC897WLk", t)
    act4 = model.Activity("Dolphin Show", "See the scary animals do tricks in the water. ", "https://source.unsplash.com/fgKEqVzX5zM", t)
    activities = {
        "Jungle Cruise": act1,
        "Guided Wilderness Hike": act2, 
        "Petting Park": act3, 
        "Dolphin Show": act4
    }

    return render_template("main/schedule.html", activity=activities[activity_name])
