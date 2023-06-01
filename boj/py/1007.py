from itertools import combinations
import math

T = int(input())

ret = []
for _ in range(T):
    N = int(input())
    P = []

    x_sum = 0
    y_sum = 0
    for i in range(N):
        P.append(list(map(int, input().split())))

        x_sum += P[i][0]
        y_sum += P[i][1]

    min_sum = 200000 * N + 1
    for l in combinations(P, N // 2):
        xs = x_sum
        ys = y_sum
        for x, y in l:
            xs -= 2 * x
            ys -= 2 * y

        d = math.sqrt(xs * xs + ys * ys)
        if d < min_sum:
            min_sum = d

    ret.append(str(min_sum))

print('\n'.join(ret))