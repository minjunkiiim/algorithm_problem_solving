t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    k = min(s)
    i = n - 1
    while i >= 0:
        if s[i] == k:
            break
        i -= 1

    new_s = k + s[:i] + s[i + 1:]

    print(new_s)