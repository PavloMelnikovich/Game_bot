from pymongo import MongoClient

mongodb = "mongodb+srv://Gosha:CSWN23zgHAd81lEh@cluster0.d4qarje.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb)
database = client.get_database("default")
users_collection = database.get_collection("users")

all_users = users_collection.find({})
for user in all_users:
    print(user)