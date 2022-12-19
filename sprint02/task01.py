def double_string(data):
    counter = 0
    for i in data:
        for y in data:
            if y + y in i and len(y + y) == len(i) or y + data[1] in i:
                counter += 1
                break
    return counter
