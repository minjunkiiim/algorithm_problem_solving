t = int(input())

for _ in range(t):
    n = int(input())
    a = [0, 0, 0, 0]
    s = 0

    i = 1
    while s + i <= n:
        s += i 
        a[i % 4] += i
        i += 1

    a[i % 4] += (n - s)

    print(a[0] + a[1], a[2] + a[3])