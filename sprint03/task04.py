def divisor(n):
    for _ in range(1, n + 1):
        if n / _ == int(n / _):
            yield _
    while True:
        yield None
