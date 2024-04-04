from django.conf import settings
import pymongo

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
        collection = self.getCollection()
        documents = collection.find({})
        return documents

    def getByAttribute(self, attribute, value):
        collection = self.getCollection()
        documents = collection.find({attribute: value})
        return documents

    def insert(self, document) -> None:
        collection = self.getCollection()
        collection.insert_one(document)

    def delete(self, documentId) -> None:
        collection = self.getCollection()
        collection.delete_one({"_id": documentId})

    def deleteAll(self) -> None:
        collection = self.getCollection()
        collection.delete_many({})

