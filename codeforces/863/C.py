def bf():

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split(' ')))

    Fib = [1, 1]
    for i in range(1, n):
        Fib.append(Fib[i - 1] + Fib[i])

    a = [-1] * n
    a[0] = b[0]
    a[n - 1] = b[n - 2]

    for i in range(1, n - 1):
        a[i] = min(b[i - 1], b[i])        


    print(' '.join(list(map(str, a))))


    1 1 2 3 5 8 13 21 34 