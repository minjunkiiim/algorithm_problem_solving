t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split(' ')))

    matrix = [x[:] for x in [[0] * n] * m]

    for i in range(n):
        arr = list(map(int, input().split(' ')))

        for j in range(m):
            matrix[j][i] = arr[j]

    for j in range(m):
        matrix[j].sort()

    ret = 0

    for i in range(n):
        num = 0
        for j in range(m):
            num += matrix[j][i]
        
        ret += num * (2 * i - n + 1)

    print(ret)