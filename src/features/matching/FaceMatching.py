from src.persistence.data_source import DataSource


class FaceMatching:
    def __int__(self, face_repo: DataSource):
        self.face_repository = face_repo

    def is_face_exist(self, face_data: int):
        data = self.face_repository.read(face_data)
        return data is not None

    def get_face_data(self, face_data: int) -> DataSource:
        return self.face_repository.read(face_data)
