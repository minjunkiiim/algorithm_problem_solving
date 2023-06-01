t = int(input())

ret = []
for _ in range(t):
    n, w, h = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    d = w - h

    min_c = b[0] - a[0]
    max_c = b[0] - a[0]

    r = 'YES'
    for i in range(1, n):
        c = b[i] - a[i]
        if c < min_c:
            if max_c - c > 2 * d:
                r = 'NO'
                break
            min_c = c

        if c > max_c:
            if c - min_c > 2 * d:
                r = 'NO'
                break
            max_c = c

    ret.append(r)

print('\n'.join(ret))