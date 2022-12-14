def kthTerm(n, k):
    l = []
    l2 = []
    for i in range(10):
        for _ in l2:
            l.append(_)
        l2 = []
        if i > 0:
            for y in l:
                l2.append(n ** i + y)
        l.append(n ** i)
    return l[k-1]


print(kthTerm(3, 4))
print(kthTerm(3, 7))
print(kthTerm(3, 3))
print(kthTerm(2, 7))
print(kthTerm(4, 3))
print(kthTerm(30, 100))
print(kthTerm(2, 1))
print(kthTerm(15, 50))
print(kthTerm(21, 63))
print(kthTerm(10, 99))
