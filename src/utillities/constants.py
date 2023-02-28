from enum import Enum
from os import path


class Constants(Enum):
    class DBConstants(Enum):
        CRED_PATH = path.join('..', '..', 'res', 'db_cred.json')
        CRED_PAIR = ("username", "password")
        DB_COLLECTION_VISITOR = ''
        DB_COLLECTION_STAFF = ''

    class WorkType(Enum):
        WORK_TYPE_1 = "WorkType1"
        WORK_TYPE_2 = "WorkType2"
