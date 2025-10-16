import json


class ConfigReader:
    PATH_JSON = '/config/config.json'

    def __init__(self, file_path=PATH_JSON):
        self.config = self._load_config(file_path)

    @staticmethod
    def _load_config(file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get(self, key: str, default = None, root_key: str = None):
        if root_key:
            root = self.config.get(root_key, default)
            return root.get(key, default)
        return self.config.get(key, default)