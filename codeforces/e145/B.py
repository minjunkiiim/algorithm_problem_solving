t = int(input())

for _ in range(t):
    n = int(input())

    L = 0
    U = n
    M = (L + U + 1) // 2
    while L + 1 < U:
        if M * M >= n:
            U = M
        else:
            L = M
        
        M = (L + U + 1) // 2

    print(M - 1)

