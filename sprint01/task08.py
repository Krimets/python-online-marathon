def studying_hours(a):
    final_counter = 0
    counter = 0
    b = -1
    for i in a:
        if int(i) >= b:
            counter += 1
        else:
            if final_counter < counter:
                final_counter = counter
            counter = 1
        b = i
    if final_counter == 0:
        return counter
    else:
        return final_counter


print(studying_hours([2, 2, 1, 3, 4, 1]))
print(studying_hours([2, 2, 9]))
