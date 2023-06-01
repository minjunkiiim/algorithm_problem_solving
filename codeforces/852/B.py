t = int(input())

for _ in range(t):
    x, y = list(map(int, input().split(' ')))

    n = 2 * (x - y)

    ret = []
    for i in range(y, x):
        ret.append(i)
    for i in range(x, y, -1):
        ret.append(i)
    print(n)
    print(' '.join(map(str, ret)))