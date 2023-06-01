t = int(input())

for _ in range(t):
    n, k, x = list(map(int, input()))
    a = list(map(int, input()))
    for i in range(n):
        a[i] -= x

    sum_list = [x[:] for x in [[0] * (n + 1)] * k + 1]
    max_sum = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            sum_list[i][j] = sum_list[i - 1][j - 1]

