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

    def __get_collection(self):
        conn = self.__get_connection()
        collection = conn[self.collection]
        return collection
    
    #CRUD

    def list(self):
        documents = []
        for doc in self.__get_collection().find({}):
            id = doc.pop('_id')
            doc['id'] = str(id)
            documents.append(doc)
        return documents
    
    def getById(self, document_id):
        document = self.__get_collection().find({"_id": ObjectId(document_id)})
        return document
        
    def filterByAttribute(self, attribute, value):
        if attribute in ('id', '_id'):
            return self.getById(value)

        if attribute in ('temperature', 'atmospheric_pressure', 'humidity', 'precipitation_percentage'):
            value = float(value) 

        documents = self.__get_collection().find({attribute: value})
        return list(documents)
        
    def insert(self, document) -> None:
        self.__get_collection().insert_one(document)

    def update(self, document_id, update_data):
        self.__get_collection().update_one(
            {"_id": ObjectId(document_id)},
            {"$set": update_data}
        )
        return self.getById(document_id)
    
    def delete(self, document_id) -> None:
        self.__get_collection().delete_one({"_id": ObjectId(document_id)})
 
    def deleteAll(self) -> None:
        self.__get_collection().delete_many({})
