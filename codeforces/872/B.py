t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    k = n * m

    b = list(map(int, input().split())) 
    b.sort()

    short = min(m, n)
    ret = (k - short) * (b[k - 1] - b[0])
    ret += (short - 1) * max(b[k - 1] - b[1], b[k - 2] - b[0])

    print(ret)