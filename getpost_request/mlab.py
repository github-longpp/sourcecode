# mongodb+srv://admin:admin@cluster0-w22fu.mongodb.net/database01?retryWrites=true
import mongoengine

db = 'database01'
username = 'admin'
password = 'admin'
host = 'mongodb+srv://admin:admin@cluster0-w22fu.mongodb.net/database01?retryWrites=true'

def connect():
    mongoengine.connect(db, host=host, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())