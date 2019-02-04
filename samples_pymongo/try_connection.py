from pymongo import MongoClient

client = MongoClient()
db = client.sample_pymongo
users = db.users

user1 = {'name': 'Artur', 'password': 'pass', 'favorit_number': 7, "hobbies": ['python', 'java', 'macos', 'linux']}

user_id = users.insert_one(user1).inserted_id
print(user_id)

insert_multiple_users = [{'name': 'Manu', 'password': 'pass', 'favorit_number': 7, "hobbies": ['barbie', 'polly']},
                         {'name': 'Catia', 'password': 'pass', 'favorit_number': 7, "hobbies": ['gym']}]

results = users.insert_many(insert_multiple_users)

# print(results)
print(results.inserted_ids)