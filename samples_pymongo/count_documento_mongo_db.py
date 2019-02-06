from pymongo import MongoClient


client = MongoClient()
db = client.sample_pymongo
Users = db.users

print(Users.find().count())

print(Users.find({'favorit_number': 7}).count())
