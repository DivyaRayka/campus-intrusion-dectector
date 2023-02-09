from enum import Enum
from os import path


class Constants(Enum):
    DB_CRED_PATH = path.join('..', '..', 'res', 'db_cred.json')
    DB_CRED_PAIR = ("username", "password")
    DB_COLLECTION_VISITOR=''
    DB_COLLECTION_STAFF=''
