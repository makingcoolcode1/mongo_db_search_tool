
from pymongo import MongoClient
import time


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
                    formatted += f"                 {item}\n"
        
        else:
            formatted += f"{new_prefix}: {value}\n\n"
    
    return formatted

client_inp = input("Enter mongo.db connection string ")
db_inp = input("Enter db name ")
collection_input = input("Enter colleciton name ")


client = MongoClient(f"{client_inp}")
db = client[f'{db_inp}']
collection = db[f'{collection_input}']


while True:
    query = input("Enter a query or type exit to quit ")

    if query.lower() == 'exit':
        break

    try:
        cursor = collection.find({"recipe_name": query})

        for document in cursor:
            formtted_document = format_mongo(document)
            print(formtted_document)
            print()
    except Exception as e:
        print(f"ERROR: {str(e)}")


client.close()