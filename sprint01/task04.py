def findPermutation(p, q):
    r = []
    for i in range(len(q)):
        b = p.index(q[i])
        r.append(b + 1)
    return r
