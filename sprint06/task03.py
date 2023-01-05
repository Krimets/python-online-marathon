import json
import jsonschema
from jsonschema import validate
import csv


class DepartmentName(Exception):
    def __init__(self, data):
        self.data = data


class InvalidInstanceError(Exception):
    def __init__(self, data):
        self.data = data


def user_with_department(csv_file, user_json, department_json):
    new_data = {}
    old_key = ''
    with open(user_json, 'r') as f:
        data = json.load(f)
    for _ in data:
        for key in _:
            if key == "name":
                new_data[_[key]] = ['']
                old_key = _[key]
            elif key == 'department_id':
                new_data[old_key] = _[key]
    with open(department_json, 'r') as f:
        data2 = json.load(f)
    new_data2 = {}
    for _ in data2:
        for key in _:
            if key == 'id':
                new_data2[_[key]] = ['']
                old_key = _[key]
            elif key == 'name':
                new_data2[old_key] = _[key]
    new_data3 = {}
    for key in new_data2:
        for key2 in new_data:
            if key == new_data[key2]:
                new_data3[key2] = new_data2[key]
    without_dep = []
    for key in new_data:
        for key3 in new_data3:
            if key not in new_data3:
                if new_data[key] not in without_dep:
                    without_dep.append(new_data[key])
    user_schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "number"
            },
            "name": {"type": "string"
                     },
            "department_id": {
                "type": "number"
            }
        },
        "required": ['id', "name", 'department_id'],
    }

    dep_schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "number"
            },
            "name": {"type": "string"
                     },
        },
        "required": ['id', "name"],
    }
    if validate_json(data, user_schema):
        raise InvalidInstanceError('Error in user schema')
    elif validate_json(data2, dep_schema):
        raise InvalidInstanceError('Error in department schema')
    elif without_dep:
        raise DepartmentName(f"Department with id {without_dep[0]} doesn't exists")
    else:
        new_data3 = dict(sorted(new_data3.items()))
        with open(csv_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'department'))
            for key in new_data3:
                writer.writerow((key, new_data3[key]))


def validate_json(data, schema):
    try:
        for _ in data:
            validate(_, schema)
    except:
        return True
