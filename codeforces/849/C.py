t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    i = 0
    while i < n // 2:
        l = int(s[i])
        r = int(s[n - 1 - i])

        if l + r != 1:
            break

        i += 1

    print(n - 2 * i)