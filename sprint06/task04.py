import json
from json import JSONEncoder


t = [{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": [{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]
t = [{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": ["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": ["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": {"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}}]

class Student:
    def __init__(self, full_name:str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'

    def serialize_to_json(self, json_file2):
        b = json.dumps(self, default=lambda o: o.__dict__)
        with open(json_file2, 'w') as f2:
            f2.write(b)
        #return b

    @staticmethod
    def from_json(json_file):
        with open(json_file) as json_file:
            json_data = json.load(json_file)
            return Student(**json_data)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title[:-5]
        self.students = students

    def __str__(self):
        ll_new = []
        try:
            for Student in self.students:
                new_l = []
                for key in Student:
                    new_l.append(Student[key])
                string_new = f'{new_l[0]} ({new_l[1]}): {new_l[2]}'
                ll_new.append(string_new)
            return f'{self.title}: {ll_new}'
        except:
            new_l = []
            for key in self.students:
                new_l.append(self.students[key])
            return f'{self.title}: ["{new_l[0]} ({new_l[1]}): {new_l[2]}"]'


    @staticmethod
    def create_group_from_file(json_file):
        with open(json_file) as json_file:
            json_data = json.load(json_file)
            if json_file.name == "2020-01.json":
                json_data = [json_data]
            return Group(json_file.name, json_data)

    @staticmethod
    def serialize_to_json(l:list, json_file2):
        b = json.dumps(l, default=lambda o: o.__dict__)
        with open(json_file2, 'w') as f2:
            f2.write(b)



g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2],"g1")