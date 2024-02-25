
from pymongo import MongoClient

print("\n**WELCOME TO THE MONGO.DB SEARCH TOOL**")
print("\nYou may type 'quit' at anytime to exit the program ")


clientInput = input("\nEnter your mongo.db connection string")
dbInput = input("\nEnter your database name to search")
collectionInput = input("\nEnter your collection to search")


try:
    clientTest = MongoClient(clientInput)
    dbTest = clientTest.get_database(dbInput)
    collectionTest = dbTest.get_collection(collectionInput)

    collection_name = dbTest.list_collection_names()

    if collection_name:
        print("\n Successfully Connected to Mongodb Database..")
        print("Collections in database are:", collection_name)
    else:
        print("Successfully connected to the database but the database is empty")
except Exception as e:
    print("\nERROR: Failed to connect to the database")
    print(f"\n ERROR: {str(e)}")

client = (f"{clientInput}")
db = [f"{dbInput}"]
collectionInput = [f"{collectionInput}"]


while True:
    operatorInput = input("Enter a mongo.db operator to search: ")
    if operatorInput.lower() == "exit":
        exit("Exiting Program.....")
    
    queryInput = input("Enter a search query")
    if queryInput.lower() == "exit":
        exit("Exiting Program......")
        