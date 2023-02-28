from abc import ABC
from typing import Any
from imutils.video import VideoStream


class CameraStream(ABC):
    __handle = None

    def get_instance(self, url: str) -> Any:
        # For now let it be like a camera simple functionality
        if url == '':
            self.__handle = VideoStream()
        return self

    def get_current_frame(self) -> Any:
        current_frame = self.__handle.read()
        return current_frame
