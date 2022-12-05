from . import db
import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    genus = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    diet = db.Column(db.String(1000), nullable=False)
    habitat = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)

class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    time = db.Column(db.String(128), nullable=True)

"""
class Message:
    def __init__(self, message_id, user, text, timestamp):
        self.message_id = message_id
        self.user = user
        self.text = text
        self.timestamp = timestamp

class Activity:
    def __init__(self, name, description, img_src, time=None):
        self.name = name
        self.description = description
        self.img_src = img_src
        self.time=time

"""
