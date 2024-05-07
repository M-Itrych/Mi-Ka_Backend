from pymongo import MongoClient
def connect_to_mongodb():
    client = MongoClient('localhost', 27017)
    db = client.data
    return client, db

def close_mongodb_connection(client):
    client.close()

def serialize_id(data):
    for d in data:
        d['_id'] = str(d['_id'])
    return data