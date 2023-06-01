t = int(input())

for _ in range(t):
    n = int(input())
    w = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    s = 0

    i = 1
    while s + i <= n:
        s += i 
        w[i % 4] += i // 2
        b[i % 4] += i // 2

        if i % 2 == 1:
            if i % 4 == 1:
                w[i % 4] += 1
            else:
                b[i % 4] += 1

        i += 1

    w[i % 4] += (n - s) // 2
    b[i % 4] += (n - s) // 2

    if (n - s) % 2 == 1:
        if i % 4 == 0 or i % 4 == 1:
            w[i % 4] += 1
        else:
            b[i % 4] += 1


    print(w[0] + w[1], b[0] + b[1], w[2] + w[3], b[2] + b[3])