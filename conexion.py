from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
"""
client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['correr']

collection.insert_one({"name":"keyboard","price":120})
"""
def insert(datos):
    client = MongoClient(MONGO_URI)

    db = client['usuarios']
    collection = db['correr']

    collection.insert_one(datos)

def traerDatos():
    
    client = MongoClient(MONGO_URI)

    db = client['usuarios']
    collection = db['correr']
    res = [datos for datos in collection.find()]
    return res