from locale import currency
import re
import flask_login
import datetime
import dateutil.tz
import uuid
import ast

from flask import Blueprint, render_template, request

from flask import Blueprint, render_template, request, redirect, url_for, flash

from . import db, bcrypt, model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    if flask_login.current_user.is_authenticated:
        return render_template("main/index_logged_in.html")
    else:
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
    return render_template("animals/animals.html", animals=animals)

@bp.route("/faq")
def faq():
    faq_items = model.Faq.query.all()
    return render_template("faq/faq.html", faq_items=faq_items)

@bp.route("/animal-info")
def animal_info():
    animal_id = request.args.get('animal', None)
    animal = model.Animal.query.filter_by(id=animal_id).first()

    return render_template("animals/animal-info.html", animal=animal)


@bp.route("/activities")
def activities():
    activities = model.ActivityPreview.query.all()
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_manager:
        return render_template("activities/activities-manager.html", activities=activities)
    else:
        return render_template("activities/activities.html", activities=activities)

@bp.route("/activity-info")
def activity_info():
    activity_id = request.args.get('activity', None)
    activity = model.ActivityPreview.query.filter_by(id=activity_id).first()

    if flask_login.current_user.is_authenticated and flask_login.current_user.is_manager:
        return render_template("activities/activity-manager-info.html", activity=activity)
    return render_template("activities/activity-info.html", activity=activity)

@bp.route("/schedule", methods=['POST', 'GET'])
@flask_login.login_required
def schedule():
    if (request.method == 'POST'):
        activity_id = request.form['actid']
        t = request.form['acttime']
        d = request.form['actdate']
 
        #creating new activity object adding it to db
        activity_preview = model.ActivityPreview.query.filter_by(id=activity_id).first()
        new_id = str(uuid.uuid1())
        new_activity = model.Activity(id=new_id, name=activity_preview.name, description=activity_preview.description, img=activity_preview.img, time=t, date=d)

        db.session.add(new_activity)
        db.session.commit()

    #update activities field for logged in user.
        user_activity_ids_str = flask_login.current_user.activities
        if user_activity_ids_str == None:
            user_activity_ids = []
        else:
            user_activity_ids = ast.literal_eval(user_activity_ids_str)

        user_activity_ids.append(str(new_id))
        user_activity_list = get_user_activities(user_activity_ids)

        flask_login.current_user.activities = str(user_activity_ids)
        db.session.commit()

        return render_template("main/schedule.html", activities=user_activity_list)
    else:
        user_activity_ids_str = flask_login.current_user.activities
        if user_activity_ids_str == None:
            user_activity_ids = []
            return render_template("main/empty_schedule.html")
        else:
            user_activity_ids = ast.literal_eval(user_activity_ids_str)
            user_activity_list = get_user_activities(user_activity_ids)
            return render_template("main/schedule.html", activities=user_activity_list)

def get_user_activities(user_activity_ids):
    user_activity_list = []
    for act_id in user_activity_ids:
        activity = model.Activity.query.filter_by(id=act_id).first()
        user_activity_list.append(activity)
    return user_activity_list