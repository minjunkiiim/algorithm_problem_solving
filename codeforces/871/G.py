t = int(input())

pyramid = []

num = 1
for i in range(1, 2024):
    l = []
    
    for k in range(i):
        l.append(num * num)
        num += 1
    
    pyramid.append(l)

rowsum = [0] * 2023
rowsum[0] = 1

for i in range(1, 2023):
    s = sum(pyramid[i])
    rowsum[i] = rowsum[i - 1] + s

rets = []
for _ in range(t):
    n = int(input())

    nsqr = n * n

    l = 0
    u = 2023
    while l + 1 < u:
        m = (l + u) // 2
        if pyramid[m][0] <= nsqr:
            l = m
        else:
            u = m
    row = l

    l = 0
    u = len(pyramid[row])
    while l + 1 < u:
        m = (l + u) // 2
        if pyramid[row][m] <= nsqr:
            l = m
        else:
            u = m
    col = l

    sum = 0

    l = col + 1
    r = col + 1

    for k in range(row, -1, -1):
        l = max(0, l - 1)
        r = min(len(pyramid[k]), r)

        if l == 0 and r == len(pyramid[k]):
            sum += rowsum[k]
            break

        for i in range(l, r):
            sum += pyramid[k][i]

    rets.append(str(sum))

print('\n'.join(rets))