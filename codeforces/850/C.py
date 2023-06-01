t = int(input())

ret = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a.sort()

    r = max(a[0] - 1, 0)
    a[0] -= r
    for i in range(1, n):
        d = a[i] - a[i - 1]
        if d > 1:
            r += d - 1
            a[i] -= d - 1

    ret.append(str(r))

print('\n'.join(ret))