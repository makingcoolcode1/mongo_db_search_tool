
from pymongo import MongoClient


def format_mongo(document, prefix = ''):
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
                    formatted += f"           {item}\n"
        
        else:
            formatted += f"{new_prefix}: {value}\n\n"

    
    return formatted




while True:
    client_inp = input("Enter your mongo.db connection string or type exit to quit ")
        
    if client_inp.lower() == "exit":
        break
        
    db_inp = input("Enter your mongo.db database name ")
    collection_inp = input("Enter your mongo.db collection name ")


    client = MongoClient(f"{client_inp}")
    db = client[f"{db_inp}"]
    collection = db[f"{collection_inp}"]
        
    while True:
        operator = input("Enter your mongo.db operator or type exit to quit ")
        
        if operator.lower() == "exit":
            exit(0) 

        query = input("Enter your search query or type exit to quit ")
        
        if query.lower() == "exit":
            exit(0)


        try:
            mongo_search = collection.find({operator: query})
            recipe_found = False


            for document in mongo_search:
                formatted_document = format_mongo(document)
                print()
                print(formatted_document)
                print()
            
            if not recipe_found:
                print("ERROR: No result found from database")
            
        except Exception as e:
            print(f"ERROR: {str(e)} ")