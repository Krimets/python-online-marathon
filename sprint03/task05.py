def logger(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        return a
    return wrapper

@logger
def concat(*args, **kwargs):
    x = ''
    s = [x for x in args]
    s1 = [kwargs[key] for key in kwargs]
    for y in s1:
        s.append(y)
    for i in s:
        if s[-1] == i:
            x += str(i)
        else:
            x += str(i) + ', '
    print(f'Executing of function concat with arguments ', x, '...', sep='')
    b = ''
    for _ in s:
        b += str(_)
    return b


@logger
def sum(a, b):
    print(f'Executing of function sum with arguments ', a, ', ', b, '...', sep='')
    return a + b


@logger
def print_arg(arg):
    print(arg)
    print(f'Executing of function print_arg with arguments ', arg, '...', sep='')


print(concat(1))
print(concat('first string', second = 2, third = 'second string'))
print(sum(2,3))
