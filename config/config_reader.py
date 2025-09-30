import json

class ConfigReader:
    PATH_JS = 'config/config.json'

    def __init__(self, file_path=PATH_JS):
        self.config = self._load_config(file_path)

    def _load_config(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get(self, key: str, default=None):
        return self.config.get(key, default)