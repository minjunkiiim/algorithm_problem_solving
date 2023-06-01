t = int(input())

for _ in range(t):
    a, b, c, d = list(map(int, input().split(' ')))

    dx = c - a
    dy = d - b

    if dy < 0 or dx > dy:
        print(-1)

    else:
        print(dy + dy - dx)