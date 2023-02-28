from typing import Any

from .data_source import DataSource
from ..models.model import Model


class CRUD:
    __db_instance: DataSource = None

    def __init__(self, source: DataSource):
        CRUD.__db_instance = source

    def store_data(self, model: Model) -> Any:
       return self.__db_instance.create(model)

    def read_data(self, field: str) -> Any:
        self.__db_instance.read(field)

    def update_data(self, old_value: str, new_value: str) -> Any:
       return self.__db_instance.update(old_value, new_value)

    def delete_data(self, field: str) -> Any:
        return self.__db_instance.delete(field)
