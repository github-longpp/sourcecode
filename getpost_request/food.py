from mongoengine import Document, StringField

class Food(Document):
    title =  StringField()
    link  = StringField()
    