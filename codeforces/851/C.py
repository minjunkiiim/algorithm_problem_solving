t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print('NO')
        continue

    a = [(i * 2) % n + 1 for i in range(n)]
    b = [(n + n // 2 - i) % n + 1 + n for i in range(n)]


    print('YES')
    for i in range(n):
        print(a[i], b[i])

