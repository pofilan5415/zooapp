from . import db

class User(db.Model):
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

"""
class Message:
    def __init__(self, message_id, user, text, timestamp):
        self.message_id = message_id
        self.user = user
        self.text = text
        self.timestamp = timestamp

class User:
    def __init__(self, user_id, email, name):
        self.user_id = user_id
        self.email = email
        self.name = name

class Animal:
    def __init__(self, animal_id, name, genus, description=None, img_src=None):
        self.animal_id = animal_id
        self.name = name
        self.genus = genus
        self.description = description
        self.img_src = img_src

class FaqItem:
    def __init__(self, faq_id, title, description):
        self.faq_id = faq_id
        self.title = title
        self.description = description
"""