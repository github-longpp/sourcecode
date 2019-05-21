import pymongo
import dns

#1 Connect database
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-w22fu.mongodb.net/mydb?retryWrites=true")

#2 Get default database
db = client.get_default_database()

#3 Get collection
posts = db["posts"]
movies = db["movies"]

#4 Create data
new_post = {
    "title" : "ABC",
    "content" : "DEF",
}

new_movie = {
    "title": "Batman",
    "rating": 8.0,
}

# 5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

#5.1 Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    print(p["title"])
    print(p["content"])



#6 CLose connection
client.close()
