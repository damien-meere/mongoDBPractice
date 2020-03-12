import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MondoDB: %s") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#Inserting a new record
#new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
#coll.insert(new_doc)

#Inserting a multiple new records
#new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},
#            {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1952', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]
#coll.insert_many(new_docs)

#Delete a single record
#documents = coll.find({'first': 'douglas'})
#coll.delete_one({'first': 'douglas'})

#Update Record
#coll.update_one({'first': 'douglas'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find()

for doc in documents:
    print(doc)


