t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(str((2 ** 32 * i) * m + (2 ** 16 * j)))

    print(n * m)
    for line in matrix:
        print(' '.join(line))