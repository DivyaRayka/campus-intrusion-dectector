from abc import ABC
from abc import abstractmethod
from typing import Any

from models.model import Model


class DataSource(ABC):

    @abstractmethod
    def create(self, model: Model):
        pass

    @abstractmethod
    def read(self, field_data: str | Any):
        pass

    @abstractmethod
    def update(self, old_field_data: str, new_field_data: str):
        pass

    @abstractmethod
    def delete(self, field_data: str):
        pass
