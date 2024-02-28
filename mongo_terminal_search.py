
from pymongo import MongoClient

def format_mongo(document, prefix = ""):
    formatted = ""

    for key, value in document.items():
        new_prefix = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            formatted += format_mongo(value, new_prefix)
        elif isinstance(value, list):
            formatted += f"{new_prefix}\n"

            for item in value:
                if isinstance(item, dict):
                    formatted += format_mongo(item, new_prefix)
                else:
                    formatted += f"            {item}\n\n"

        else:
            formatted += f"{new_prefix}:{value}\n"
    
    return formatted


print("\n** WELCOME TO THE MONGO.DB CONNECTION TOOL **")

connected = False

while not connected:

    clientInput = input("\n\nEnter your mongo.db connection string: ")


    dbInput = input("\nEnter your database name: ")
    collectionInput = input("\nEnter your collection name: ")

    try:
        clientTest = MongoClient(clientInput)
        dbTest = clientTest.get_database(dbInput)
        collectionTest = dbTest.get_collection(collectionInput)

        testMongoConnection = dbTest.list_collection_names()

        if testMongoConnection:
            print("\nSuccessfully connected to the mongo.db database!")
            print('\nCollections in the database include:', testMongoConnection)
            connected = True
        else:
            print("/Successfully connected to the mongo.db database but it is empty!")
            connected = True

    except Exception as e:
        print("\nERROR: Failed to connect to the mongo.db database!")
        print(f"\nERROR: {str(e)}")
        connected = False

while True:
    operatorInput = input("\nEnter your operator to search: ")
    queryInput = input("\nEnter a search query: ")

    try:
        client = MongoClient(clientInput)
        db = client[f"{dbInput}"]
        collecion = db[f"{collectionInput}"]

        searchDatabase = collecion.find({operatorInput:queryInput})

        for document in searchDatabase:
            formatted_document = format_mongo(document)
            print(formatted_document)
    
    except Exception as e:
        print(f"ERROR: {str(e)}")

        
