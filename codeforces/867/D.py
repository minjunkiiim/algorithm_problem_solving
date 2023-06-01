t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue
    if (n * (n + 1) // 2) % n == 0:
        print(-1)
        continue

    ret = []
    ret.append(n)

    for i in range(1, n):
        if i % 2 == 0:
            ret.append(i)

        else:
            ret.append(n - i)

    print(' '.join(list(map(str, ret))))