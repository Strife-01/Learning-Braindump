def power(l):
    if len(l) == 0:
        return [[]]
    ll = power(l[1:])
    ps = []
    for cl in ll:
        ps.append([l[0]] + cl)
        ps.append(cl)
    return ps
