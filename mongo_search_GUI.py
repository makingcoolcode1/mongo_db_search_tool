
from tkinter import *
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
                if isinstance(value, dict):
                    formatted += format_mongo(value, new_prefix)
                else:
                    formatted += f"             {item}\n"
        
        else:
            formatted += f"{new_prefix}: {value}\n\n"
    
    return formatted



def search_mongo():
    client_search = client_inp.get()
    db_search = db_inp.get()
    collection_search = collection_inp.get()
    query = query_inp.get()
    search_result.delete(1.0, END)

    try:

        client = MongoClient(f"{client_search}")
        db = client[f"{db_search}"]
        collection = db[f"{collection_search}"]

        cursor = collection.find({"recipe_name": query})

        for document in cursor:
            formatted_document = format_mongo(document)
            search_result.insert(END, formatted_document)
            search_result.insert(END, "\n\n")
    
    except Exception as e:
        search_result.insert(END, f"ERROR: {str(e)}")



root = Tk()
root.title("Mongo.db Search")
root.geometry('1200x900')
root.resizable(0,0)


#Frame

search_frame = Frame(root, background="#7CCD7C", width=400, height=600)
search_frame.place(x=25, y=100)


#Labels

client_lbl = Label(search_frame, text="Enter URL Connection String", font=('arial', 12, 'bold'), bg="#7CCD7C")
client_lbl.place(x=85, y=30)

db_lbl = Label(search_frame, text="Enter Your mongo.db Database Name", font=('arial', 12, 'bold'), bg="#7CCD7C")
db_lbl.place(x=50, y=120)

collection_lbl = Label(search_frame, text="Enter Your mongo.db Collection", font=('arial', 12, 'bold'), bg="#7CCD7C")
collection_lbl.place(x=70, y=210)

operator_lbl = Label(search_frame, text="Enter Your mongo.db Operator", font=('arial', 12, 'bold'), bg="#7CCD7C")
operator_lbl.place(x=70, y=300)

query_lbl = Label(search_frame, text="Enter Your mongo.db Search Query", font=('arial', 12, 'bold'), bg="#7CCD7C")
query_lbl.place(x=70, y=390)


#Var inputs

client_inp = Entry(search_frame, width=40, font=('arial', 12))
client_inp.place(x=15, y=60)

db_inp = Entry(search_frame, width=40, font=('arial', 12))
db_inp.place(x=15, y=150)

collection_inp = Entry(search_frame, width=40, font=('arial', 12))
collection_inp.place(x=15, y=240)

operator_inp_inp = Entry(search_frame, width=40, font=('arial', 12))
operator_inp_inp.place(x=15, y=330)

query_inp = Entry(search_frame, width=40, font=('arial', 12))
query_inp.place(x=15, y=420)


#Search Button and Result

search_btn = Button(search_frame, text="Search", command=search_mongo)
search_btn.place(x=160, y=500)


search_result = Text(root, width=80, height=50, font=("arial", 12))
search_result.place(x=450, y=5)







def enter_press(search):
    search_btn.invoke()
root.bind("<Return>", enter_press)


root.mainloop()


#mongodb+srv://zachgedge:wranglerjetta1@cluster0.kvykuob.mongodb.net/


