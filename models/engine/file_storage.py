import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj

    def save(self):
        serialized_obj = {"__objects":self.__objects}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        try:
            if self.__file_path:
                with open(self.__file_path, 'r') as file:
                    deserialize = json.load(file)
                return deserialize
        except FileNotFoundError:
            pass