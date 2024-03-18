from model import baseModel


class filestorage:
    __file__path = "file.json"
    __objects = {}

    def save(self):
        serialized_obj = {}
        for key,value in self.__objects.items:
            serialized_obj[key] = obj.dict