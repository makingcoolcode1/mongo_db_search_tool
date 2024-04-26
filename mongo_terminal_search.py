
from pymongo import MongoClient
from format_mongo import format_mongo

print("\n**Welcome to the Mongo.db search tool**")
print("Type 'exit' at anytime to quit")

connected = False


while not connected:

    connectionInput = input("\nEnter your mongo.db connection string: ")
    if connectionInput.lower() == "exit":
        exit("Exiting Program....")

    dbInput = input("\nEnter your database name: ")
    if dbInput.lower() == "exit":
        exit("Exiting Program....")

    collectionInput = input("Enter your collection name: ")
    if collectionInput.lower() == "exit":
        exit("Exiting Program....")

    print("\nConnecting, Please wait..........")

    try:
        client = MongoClient(connectionInput)
        db = client.get_database(dbInput)
        collection = db.get_collection(collectionInput)

        testConnection = db.list_collection_names()

        if testConnection:
            print("\nSuccessfully connected to the database")
            connected = True
        else:
            print("Successfully connected, but the database is empty, Please another entry: ")
            connected = False
    except Exception as e:
        print("ERROR: Unable to connect to the database: ")
        connected = False

while True:

    operatorInput = input("\nEnter your operator to search: ")
    if operatorInput.lower() == "exit":
        exit("Exiting Program....")

    queryInput = input("\nEnter your search query: ")
    if queryInput.lower() == "exit":
        exit("Exiting Program....")

    searchQuery = collection.find({operatorInput:queryInput})

    for document in searchQuery:
        formatted_document = format_mongo(document)
        print(formatted_document)



