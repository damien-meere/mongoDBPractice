import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI")
test_mongo = os.getenv("MONGO_URI_TASK")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MondoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a Record")
    print("2. Find a Record")
    print("3. Edit a Record")
    print("4. Delete a Record")
    print("5. Exit")
    print("6. Display All Records")
    print("7. Print MONGO_URI")

    option = input("Enter an Option: ")
    return option

def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error: No results Found")

    return doc

def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document Inserted")
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": "+ v.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] :")

                if update_doc[k] == "":
                    update_doc[k] = v
                
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document Updated")
        except:
            print("Error accessing the database")

def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": "+ v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N :")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.delete_one(doc)
                print("Document Deleted")
            except:
                print("Error accessing the database")
        
        else:
            print("Document not deleted")

def display_all():
    documents = coll.find()

    if documents:
        print("")
        for doc in documents:
            print(doc)

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        elif option == "6":
            display_all()
        elif option == "7":
            print("")
            #print("MONGO_URI: "+ MONGO_URI)
            print(os.getenv("MONGO_URI_TASK"))
        else:
            print("Invalid Option")
        print("")

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
