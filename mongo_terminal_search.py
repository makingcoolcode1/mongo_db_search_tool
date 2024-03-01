
from pymongo import MongoClient
from format_mongo import format_mongo

print("** WELCOME TO THE MONGO.DB SEARCH TOOL **")
print("Type 'exit' at any time to quit")

connected = False

while not connected:

    clientInput = input("\nEnter your mongo.db connection string: ")
    if clientInput.lower() == "exit":
        exit("Exiting Mongo.db Search Tool")

    dbInput = input("\nEnter your database name: ")
    if dbInput.lower() == "exit":
        exit("Exiting Mongo.db Search Tool")

    collectionInput = input("\nEnter your collection name: ")
    if collectionInput.lower() == "exit":
        exit("Exiting Mongo.db Search Tool")

    try:
        clientTest = MongoClient(clientInput)
        dbTest = clientTest.get_database(dbInput)
        collectionTest = dbTest.get_collection(collectionInput)

        testConnection = dbTest.list_collection_names()

        if testConnection:
            print("\nConnection Successful!")
            print("\nCollections in the database include: ", testConnection)
            connected = True
        else:
            print("\nConnection Sucessful but the database is empty.......Please try again!")
            connected = False
    except Exception as e:
        print("\nERROR: Failed to connect to the database!")
        print(f"\nERROR: {str(e)}")
        connected = False

while True:
    operatorInput = input("\nEnter your operator to search: ")
    if operatorInput.lower() == "exit":
        exit("Exiting Mongo.db Search Tool")

    querySearch = input("\nEnter a search query: ")
    if querySearch.lower() == exit:
        exit("Exiting Mongo.db Search Tool")

    client = MongoClient(clientInput)
    db = client[dbInput]
    collection = db[collectionInput]

    searchMongoDb = collection.find({operatorInput:querySearch})

    for document in searchMongoDb:
        formatted_document = format_mongo(document)
        print(formatted_document)
