import json
import pickle
from enum import Enum

class FileType(Enum):
   JSON = 'json'
   BYTE = 'bin'

class SerializeManager:
    def __init__(self, filename, type):
        self.type = type
        if type == FileType.JSON:
            self.file_obj = open(filename, 'w')
        elif type == FileType.BYTE:
            self.file_obj = open(filename, 'wb')

    def serialize(self, object):
        if self.type == FileType.BYTE:
            pickle.dump(object, self.file_obj)
        elif self.type == FileType.JSON:
            json.dump(object, self.file_obj)
        else:
            self.file_obj.write(object)


    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def serialize(object, filename, fileType):
    manager = SerializeManager(filename, fileType)
    manager.serialize(object)


data = {"prop1": "value1", "prop2" : "value2"}
user = SerializeManager("test_4.json", FileType.JSON)
user.serialize(data)
with SerializeManager("test_4.json", FileType.JSON) as user:
    user.serialize(data)
# print_file("test_4.json")
