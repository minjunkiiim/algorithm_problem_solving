t = int(input())

for _ in range(t):
    n, x1, y1, x2, y2 = list(map(int, input().split(' ')))

    z1 = -1
    z2 = -1
    if x1 + y1 <= n:
        z1 = min(x1, y1)
    else:
        z1 = min((n + 1 - x1), (n + 1 - y1))
    
    if x2 + y2 <= n:
        z2 = min(x2, y2)
    else:
        z2 = min((n + 1 - x2), (n + 1 - y2))

    print(abs(z1 - z2))