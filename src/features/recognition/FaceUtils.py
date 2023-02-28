from typing import Any

import cv2


class FaceUtils:
    @staticmethod
    def get_face_hash(self, face_data: Any):
        return hash(face_data)

    @staticmethod
    def get_gray_image(self, image: Any):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
