import math

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    k = []
    for i in range(n):
        k.append(int(input()))

    k.sort()

    for i in range(m):
        a, b, c = list(map(int, input().split(' ')))

        if c <= 0:
            print('NO')
            continue

        minimum = b - math.sqrt(4 * a * c)
        maximum = b + math.sqrt(4 * a * c)

        L = 0
        R = n

        M = (L + R) // 2
        while L + 1 < R:
            if minimum < k[M] and k[M] < maximum:
                break
            
            elif k[M] <= minimum:
                L = M

            else:
                R = M
                
            M = (L + R) // 2

        if minimum < k[M] and k[M] < maximum:
            print('YES')
            print(k[M])
        else:
            print('NO') 