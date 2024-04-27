
from pymongo import MongoClient
from format_mongo import format_mongo

print("\nW**Welcome to the mongo.db search tool**")
print("\nType 'exit' at anytime to quit")

connected = False

while not connected:

    clientInput = input("\nEnter your mongo.db connection string: ")
    dbInput = input("\nEnter your database name: ")
    collectionInput = input("\nEnter your collecion name: ")

    try:
    
        client = MongoClient(clientInput)
        db = client.get_database(dbInput)
        collection = db.get_collection(collectionInput)

        testConnection = db.list_collection_names()

        print("\nConnecting....Please Wait........")

        if testConnection:
            print("\nSuccessfully connected to the Mongo.db database!")
            print("\n Collections in database include:", testConnection)
            connected = True
        else:
            print("\nSuccessfully connected to the database but it is empty! Please enter anoter databaseL ")
            connected = False
    
    except Exception as e:
        print("\nERROR: Failed to connect to the database.....Please enter a valid database. ")
        print(f"{str(e)}")
        connected = False


while True:

    operatorInput = input("\nEnter your operator to search: ")
    if operatorInput.lower() == "exit":
        exit("Exiting Program....")

    queryInput = input("\nEnter your search query: ")
    if queryInput.lower() == "exit":
        exit("Exiting Program....")

    searchMongo = collection.find({operatorInput:queryInput})


    for document in searchMongo:
        formatted_document = format_mongo(document)
        print(formatted_document)

    