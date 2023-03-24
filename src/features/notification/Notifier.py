from typing import Any


class Notification:
    def __init__(self, source):
        self.source = source

    def notify(self, message: str) -> str:
        if self.source:
            return message
        raise Exception('Source not defined')
