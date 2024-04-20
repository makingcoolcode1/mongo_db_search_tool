
from pymongo import MongoClient
from format_mongo import format_mongo

print("\n**Welcome to the mongo.db search tool**")
print("Type 'exit' at any time to quit the application\n")


## Set boolean to continue if connection = False or break if connection = True in while loop
connected = False

while not connected:
    
    ## User input for db info....Type 'exit' to quit
    connectionInput = input("\nEnter your mongo.db connection string: ")
    if connectionInput.lower() == "exit":
        exit("Exiting Program.....")

    dbInput = input("\nEnter your database name: ")
    if dbInput.lower() == "exit":
        exit("Exiting Program.....")

    collectionInput = input("\nEnter your collection mame: ")
    if collectionInput.lower() == "exit":
        exit("Exiting Program.....")

        
    ## Attempt to connect to database, show success/fail results
    try:
    
        client = MongoClient(connectionInput)
        db = client.get_database(dbInput)
        collection = db.get_collection(collectionInput)

        print("\nConnecting...Please wait...........")

        testConnection = db.list_collection_names()

        if testConnection:
            print("Successfully connected to the mongo.db database!")
            connected = True
        else:
            print("Successfully connected to the mongo.db database, but the database is empty! Please enter another database: ")
            connected = False
    
    except Exception as e:
        print("ERROR! Failed to connect to the mongo.db database:")
        print(f"{str(e)}")
        connected = False


while True:
    try:
        operatorInput = input("\nEnter an oprator to search: ")
        if operatorInput.lower() == "exit":
            exit("Exiting Program....")

        queryInput = input("\nEnter a search query: ")
        if queryInput.lower() == "exit":
            exit("Exiting Program")


        searchMongo = collection.find({operatorInput:queryInput})

        queryFound = False
        for document in searchMongo:
            formatted_document = format_mongo(document)
            print(formatted_document)
            queryFound = True
        
        if not queryFound:
            print("ERROR: No results found")

    except KeyboardInterrupt:
        print("\nExiting Program....")
        exit()
    except Exception as e:
        print(f"ERROR{str(e)}")
        exit()


