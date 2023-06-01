T = int(input())

for _ in range(T):
    x = list(map(int, input().split(' ')))

    x.sort()

    d1 = x[2] - x[0]
    d2 = x[2] - x[1]

    if d1 % 2 == 1 or d2 % 2 == 1 or (d1 + d2) % 6 != 0:
        print(-1)
    else:
        k = 0
        if d1 > d2 * 2:
            x = (d1 - 2 * d2) // 3
            d1 += x
            d2 += 2 * x
            k = (d1 + d2) // 6
        else:
            k = (d1 + d2) // 6
        print(k)
