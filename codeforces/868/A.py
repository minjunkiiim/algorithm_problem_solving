t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    m = -1
    for i in range(n // 2 + 1):
        if i * (i - 1) // 2 + (n - i) * (n - i - 1) // 2 == k:
            m = i
            break

    if m < 0:
        print('NO')

    else:
        print('YES')
        print(' '.join([str(-1)] * m + [str(1)] * (n - m)))