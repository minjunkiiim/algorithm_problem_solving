t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ldict = {}
    rdict = {}

    for c in s:
        rdict[c] = rdict.get(c, 0) + 1

    ret = len(rdict.keys())
    for c in s:
        ldict[c] = ldict.get(c, 0) + 1

        rdict[c] -= 1
        if rdict[c] <= 0:
            rdict.pop(c)

        size = len(ldict.keys()) + len(rdict.keys())
        if size > ret:
            ret = size

    print(ret)