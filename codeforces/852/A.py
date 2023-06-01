t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split(' ')))
    n, m = list(map(int, input().split(' ')))

    ret = min(b * n, a * m * (n // (m + 1)) + min(min(a, b) * (n % (m + 1)), a * m))

    print(ret)