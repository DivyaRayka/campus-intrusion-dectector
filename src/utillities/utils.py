import json


class Utilities:
    @staticmethod
    def get_db_cred(credential_path: str, retrieval_keys: tuple) -> tuple:
        data = Utilities.__get_json_obj(credential_path)
        return data[retrieval_keys[0]], data[retrieval_keys[1]]

    @staticmethod
    def __get_json_obj(path: str):
        f = open(path, 'r')
        data = json.load(f)
        f.close()
        return data
