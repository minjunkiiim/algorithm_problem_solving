t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    p = list(map(int, input().split(' ')))

    r = ['-1'] * n

    s = set()

    for i in range(m):
        if p[i] not in s:
            r[n - 1 - len(s)] = str(i + 1)
        s.add(p[i])
        if len(s) >= n:
            break

    ret = ' '.join(r)
    print(ret)