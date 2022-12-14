def order(a):
    counter_as = 0
    counter_des = 0
    b = 0
    for i in a:
        if i > b:
            counter_as += 1
        else:
            counter_des += 1
        b = i
    if counter_as < 2:
        k = 'descending'
    elif counter_des < 2:
        k = 'ascending'
    else:
        k = 'not sorted'
    return k

order([10, 5, 4])
order([6, 20, 160, 420])
order([6, 20, 160, 420])
