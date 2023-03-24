import dataclasses
import json
from typing import Any


class Utilities:
    @staticmethod
    def get_json_dump(obj: object):
        return json.dumps(obj)
