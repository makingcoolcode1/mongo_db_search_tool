
from pymongo import MongoClient


def format_mongo(document, prefix = ""):
    formtted = ""


    for key, value in document.items():
        new_prefix = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            formtted += format_mongo(value, new_prefix)
        elif isinstance(value, list):
            formtted += f"{new_prefix}\n"


            for item in value:
                if isinstance(item, dict):
                    formtted += format_mongo(item, new_prefix)
                else:
                    formtted += f"           {item}\n"
        
        else:
            formtted += f"{new_prefix}: {value}\n\n"
    
    return formtted


client_inp = input("Enter your mongo.db connection string ")
db_inp = input("Enter your mongo.db database name ")
collection_inp = input("Enter your mongo.db collection name ")


client = MongoClient(f"{client_inp}")
db = client[f"{db_inp}"]
collection = db[f"{collection_inp}"]


while True:
    criteria_inp = input("Enter the search field or type exit to quit ")
    query = input("Enter your search criteria ")

    if query.lower() == "exit":
        break

    try:
        collection_search = collection.find({criteria_inp: query})

        for document in collection_search:


            formatted_document = format_mongo(document)
            print()
            print(formatted_document)
            print()

    except Exception as e:
        print(f"ERROR: {str}")
