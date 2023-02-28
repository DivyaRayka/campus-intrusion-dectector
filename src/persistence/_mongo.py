from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.server_api import ServerApi

from .data_source import DataSource
from ..models.model import Model


class MongoConnectorService(DataSource):
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

    def create(self, model: Model) -> None:
        self.__collection.insert_one(model)

    def read(self, field_data: str) -> Mapping[str, Any]:
        document = self.__collection.find_one(field_data)
        return document

    def delete(self, field_data:str):
        document = self.__collection.find_one_and_delete(field_data)
        return document

    def update(self, old_field_data:str, new_field_data:str):
        document = self.__collection.find_one_and_update(old_field_data,new_field_data)
        return document
