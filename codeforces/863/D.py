def bf(n, x, d, Fib):
    if x == 1:
        return True

    if d > n + 1:
        return False

    num = Fib[d]

    if num > x:
        return False

    if bf(n, x - num, d + 2, Fib):
        return True
    
    if bf(n, x, d + 2, Fib):
        return True

    return False



t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split(' ')))

    Fib = [1, 1]
    for i in range(1, n + 1):
        Fib.append(Fib[i - 1] + Fib[i])

    if (bf(n, x, 2, Fib) and (bf(n, y, 1, Fib) or bf(n, y + 1, 1, Fib))) or ((bf(n, x, 1, Fib) or bf(n, x + 1, 1, Fib)) and bf(n, y, 2, Fib)):
        print('YES')
    else:
        print('NO')
