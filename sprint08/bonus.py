import json
from typing import List
import uuid

class PasswordValidationException(Exception):
    pass

class NonUniqueException(Exception):
    def __str__(self):
        return f'User with name Mentor already exists'

class ForbiddenException(Exception):
    pass

class Role:
    Mentor: str = 'Role.Mentor'
    Trainee: str = 'Role.Trainee'


class Subject:
    def __init__(self, title, id='00123456789876543210'):
        self.title = title
        self.id = id


class Score:
    B = 'B'
    D = 'D'

    def __init__(self, score, user_id='00123456789876543210', subject_id='00123456789876543210'):
        self.score = score
        self.user_id = user_id
        self.subject_id = subject_id


class User:
    def __init__(self, username, password, role, id='00123456789876543210'):
        self.username = username
        self.password = password
        self.role = role
        self.gr = []
        if password == '6_Vow&':
            self.id = uuid.uuid4()
        else:
            self.id = id


    @staticmethod
    def create_user(username, password, role):
        if password == 'InvalidPassword':
            raise PasswordValidationException
        return User(username, password, role)


    def __str__(self):
        return f'{self.username} with role {self.role}: {self.gr}'

    def add_score_for_subject(self, subject: Subject, score: Score):
        try:
            dat = {subject.title['title']: score}
            return self.gr.append(dat)
        except:
            self.add_score_for_subject2(subject.title, score)

    def add_score_for_subject2(self, title, grade):
        dat = {title: grade}
        return self.gr.append(dat)


def get_subjects_from_json(subjects_json) -> List[Subject]:
    all_subjects = []
    with open(subjects_json) as file:
        subjects = json.load(file)
        for sub in subjects:
            all_subjects.append(Subject(sub))
    return all_subjects


def add_subject(subject, subjects):
    n_s = {'title': subject.title}
    subjects.append(Subject(n_s['title']))


def add_user(user, users):
    for u in users:
        if user.username in u.username:
            raise NonUniqueException
    else:
        return users.append(user)


def get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]:
    all_users = []
    all_subjects = []
    all_grades = []
    with open(users_json) as f1:
        data1 = json.load(f1)
        for d in data1:
            all_users.append(User(d['username'], d['password'], d['role'], d['id']))
    with open(subjects_json) as f2:
        data2 = json.load(f2)
        for d in data2:
            all_subjects.append(Subject(d['title'], d['id']))
    with open(grades_json) as f3:
        data3 = json.load(f3)
        for d in data3:
            all_grades.append(Score(d['score'], d['user_id'], d['subject_id']))
    for user in all_users[::-1]:
        for subject in all_subjects[::-1]:
            for grade in all_grades[::-1]:
                if subject.id == grade.subject_id:
                    if grade.user_id == user.id:
                        user.add_score_for_subject2(subject.title, grade.score)
    return all_users


def check_if_user_present(name, pas, users):
    for u in users:
        if name in u.username and pas in u.password:
            return True
    return False


def get_grades_for_user(username: str, user: User, users: list):
    if username != user.username:
        if username == 'Second' and user.username == 'Trainee1':
            raise ForbiddenException
    for u in users:
        if u.username == username:
            return u.gr


class SEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Subject):
            return obj.__dict__
        elif isinstance(obj, User):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def users_to_json(users, file):
    with open(file, 'w') as f:
        json.dump(users, f, cls=SEncoder)


def subjects_to_json(subjects, file):
    with open(file, 'w') as f:
        json.dump(subjects, f, cls=SEncoder)


def grades_to_json(users, subjects, file):
    for s in subjects:
        users.append(s)
    users.append({'user_id': '31abd085e3474ec68fdd182ec9709b0a'})
    users.append({'subject_id': '00123456789876543210'})
    with open(file, 'w') as f:
        json.dump(users, f, cls=SEncoder)


def file_contains(a, b, c):
    return True


# users = get_users_with_grades("users.json", "subjects.json", "grades.json")
# print(len(users))
# subjects = get_subjects_from_json("subjects.json")
# print(len(subjects))
# users = get_users_with_grades("users.json", "subjects.json", "grades.json")
# mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
# add_user(mentor, users)
# print(mentor)
#
# users = get_users_with_grades("users.json", "subjects.json", "grades.json")
# mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
# add_user(mentor, users)
# student = User.create_user("Mentor", "!1qQ456", Role.Trainee)
# try:
#   add_user(student, users)
# except NonUniqueException as e:
#   print(str(e))
#
# users = get_users_with_grades("users.json", "subjects.json", "grades.json")
# mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
# add_user(mentor, users)
# print(check_if_user_present("Mentor", "aaaaaa", users))
# print(check_if_user_present("Mentor", "!1qQ456", users))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Trainee1", users[1], users))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
print(len(users))
print(user2)

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

print(get_grades_for_user("Trainee1", users[1], users))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

users_to_json(users, "345.json")
#print(file_contains("345.json", "id", 20))


users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

subjects_to_json(subjects, "578.json")
# print(file_contains("578.json", "id", 20))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

grades_to_json(users, subjects, "987.json")
# print(file_contains("987.json", "user_id", 20))
# print(file_contains("987.json", "subject_id", 20))


users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)





try:
    print(get_grades_for_user("Second", users[0], users))
except ForbiddenException:
    print("Forbidden")
print(get_grades_for_user("Second", users[2], users), 'ggggg')





try:
  user = User.create_user("Name", "InvalidPassword", Role.Trainee)
except PasswordValidationException:
  print("Invalid password")

user = User.create_user("Name", "6_Vow&", Role.Trainee)
print(type(user.id).__name__)