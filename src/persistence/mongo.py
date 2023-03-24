import dataclasses
import urllib
from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.server_api import ServerApi

from utillities.utils import Utilities
from .data_source import DataSource
from models.model import Model


class MongoConnectorService(DataSource):
    __client: MongoClient | None = None
    __db: Database | None = None
    __collection: Collection | None = None

    def __init__(self, credentials: tuple, collection: str):
        connection_str = f"mongodb+srv://{urllib.parse.quote(credentials[0])}:{urllib.parse.quote(credentials[1])}@intrusiondetectorcluste.szvltpu.mongodb.net/?retryWrites=true&w" \
                         f"=majority"
        self.__client = MongoClient(connection_str, server_api=ServerApi('1'))
        self.__db = self.__client.visit
        self.__collection = self.__db.get_collection(collection)

    def create(self, model: Model) -> None:
        self.__collection.insert_one(dataclasses.asdict(model))

    def read(self, field_data: str) -> Mapping[str, Any]:
        document = self.__collection.find_one(field_data)
        return document

    def delete(self, field_data: str):
        document = self.__collection.find_one_and_delete(field_data)
        return document

    def update(self, old_field_data: str, new_field_data: str):
        document = self.__collection.find_one_and_update(old_field_data, new_field_data)
        return document
