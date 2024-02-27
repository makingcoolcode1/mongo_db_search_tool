
from pymongo import MongoClient

print("** WELCOME TO THE MONGO.DB SEARCH TOOL **")

connected = False

while not connected:
    clientInput = input("\nEnter your mongo.db connection string: ")
    dbInput = input("\nEnter your database name: ")
    collectionInput = input("\nEnter your collection name: ")

    
    try:

        clientTest = MongoClient(clientInput)
        dbTest = clientTest.get_database(dbInput)
        collectionTest = dbTest.get_collection(collectionInput)

        testConnection = dbTest.list_collection_names()

        if testConnection:
            print("\nSuccessfully connected to the mongo.db database")
            print("\nCollections in the database include: ", testConnection)
            connected = True
        else:
            print("\nSuccessfully connected to the database but there are no collections or the database name is invalid!")
            connected = True
    except Exception as e:
        print("\nERROR: Could not connect to the database!")
        print(f"\n ERROR: {str(e)}")
        connected = False