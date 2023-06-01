t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sorted = [[a[i], i] for i in range(n)]
    a_sorted.sort()
    b.sort()

    ret = [0] * n

    for i in range(n):
        ret[a_sorted[i][1]] = str(b[i])

    print(' '.join(ret))