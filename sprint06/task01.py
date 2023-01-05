import json


data = [
    {
        "name": "Bob1",
        "pass": "_00_"
    },
    {
        "name": "Bob2",
        "pass": ["_00_", "56"]
    }
]
with open('file.json', 'w') as f:
    json.dump(data, f)


def find(file, key):
    global values
    values = []
    with open(file) as f:
        data = json.load(f)
    final = my_func(data, key)
    values = []
    return final



def my_func(data, rule):
    if type(data) == list:
        data.reverse()
        for i in data:
            try:
                my_func(i, rule)
            except:
                d = data
                values.append(d)
    else:
        for key in data:
            try:
                d = data[key]
            except:
                d = data
                if key == rule:
                    values.append(d)
                    break
            if type(d) == list:
                d.reverse()
                if key == rule:
                    for i in d:
                        if i not in values:
                            values.append(i)
                    break
                d.reverse()
                for i in d:
                    my_func(i, rule)
            elif type(d) == str:
                if key == rule:
                    if d not in values:
                        values.append(data[key])
            else:
                my_func(d, rule)
    return values


print(find("file.json", 'password'))

# import collections
#
# actual = find("file.json", 'password')
# print(actual)
# expected = ['try', '_00_']
# print(collections.Counter(actual) == collections.Counter(expected))