from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.server_api import ServerApi


class MongoConnectorService:
    __client: MongoClient | None = None
    __db: Database | None  = None
    __collection: Collection | None = None

    def __init__(self, credentials: tuple, collection: str):
        connection_str = f"mongodb+srv://{0}:{1}" \
                         f"@visitorstoragecluster.2uji5v9.mongodb.net/?retryWrites=true&w=majority" \
            .format(credentials[0], credentials[1])
        self.__client = MongoClient(connection_str, ServerApi('1'))
        self.__db = self.__client.get_default_database()
        self.__collection = self.__db.get_collection(collection)

    def create_document(self, model):
        self.__collection.insert_one(model)

    def find_document_by_field(self, field_data):
        document = self.__collection.find_one(field_data)
        return document

    def find_and_delete_document(self, field_data):
        document = self.__collection.find_one_and_delete(field_data)
        return document

    def find_and_update_document(self, old_field_data, new_field_data):
        document = self.__collection.find_one_and_update(old_field_data,new_field_data)
        return document
