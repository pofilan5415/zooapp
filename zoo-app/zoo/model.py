from . import db
import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_manager = db.Column(db.Boolean)
    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    activities=db.Column(db.ARRAY(db.String(64)), nullable=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    genus = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    diet = db.Column(db.String(1000), nullable=False)
    habitat = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    type = db.Column(db.String(128), nullable=False)

class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

class ActivityPreview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    #times = db.Column()
    #dates = db.Column()
    #is_featured = db.Column(db.Boolean)

class Activity(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    time = db.Column(db.String(128), nullable=True)
    date = db.Column(db.String(128))
