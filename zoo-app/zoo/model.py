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