
from django.conf import settings
import pymongo

class WeatherRepository:
    collection = ''
    
    def __init__(self, collectionName) -> None:
        self.collection = collectionName
        
    def getConnection(self):
        stringConnection = getattr(settings, "MONGO_CONNECTION_STRING")
        database = getattr(settings, "MONGO_DATABASE_NAME")
        client = pymongo.MongoClient(stringConnection)
        connection = client[database]
        return connection
        
    def getCollection(self):
        connection = self.getConnection()
        collection = connection[self.collection]
        return collection
        
    # CRUD
    
    def getById(self, id):
        collection = self.getCollection()
        document = collection.find_one({"_id": id})
        return document
        
    def getAll(self):
        collection = self.getCollection()
        documents = collection.find({})
        return list(documents)
    
    def getByAttribute(self, attribute, value):
        collection = self.getCollection()
        documents = collection.find({attribute: value})
        return list(documents)
    
    def insert(self, document):
        collection = self.getCollection()
        collection.insert_one(document)
    
    def delete(self, id):
        collection = self.getCollection()
        collection.delete_one({"_id": id})
    
    def deleteAll(self):
        collection = self.getCollection()
        collection.delete_many({})
