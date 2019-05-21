from mongoengine import Document, StringField, IntField

class Registration(Document):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    yob = IntField()
    gender = StringField()
    city = StringField()