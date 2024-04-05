from django.conf import settings
import pymongo
from bson import ObjectId

class WeatherRepository:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        
        stringConnection = getattr(settings, "MONGO_CONNECTION_STRING")
        database = getattr(settings, "MONGO_DATABASE_NAME")
        try:
            client = pymongo.MongoClient(stringConnection)
        except:
            raise("Error in database connection")
        connection = client[database]
        return connection

    def getCollection(self):
        connection = self.getConnection()
        collection = connection[self.collection]
        return collection

    # CRUD

    def getById(self, documentId):
        collection = self.getCollection()
        document = collection.find_one({"_id": documentId})
        return document

    def getAll(self):
        documents = []
        for document in self.getCollection().find({}):
            id = document.pop('_id')
            document['id'] = str(id)
            documents.append(document)
        return documents

    
    def getByID(self, id):
        document = self.getColletion().find_one({"_id": ObjectId(id)})
        id = document.pop('_id')
        document['id'] = str(id)
        return document
    

    def update(self, document, id):
        self.getColletion().update_one({"_id": ObjectId(id)}, document)
          

    def insert(self, document) -> None:
        collection = self.getCollection()
        collection.insert_one(document)

    def delete(self, documentId) -> None:
        collection = self.getCollection()
        collection.delete_one({"_id": documentId})

    def deleteAll(self) -> None:
        collection = self.getCollection()
        collection.delete_many({})

