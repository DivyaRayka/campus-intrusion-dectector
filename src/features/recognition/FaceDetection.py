from typing import Any
import cv2


class FaceDetection:
    def __init__(self, classifier: str):
        self.face_detector = cv2.CascadeClassifier(classifier)

    def get_faces(self, image: Any) -> list:
        faces = self.face_detector.detectMultiScale(image, 1.1, 4)
        return faces
