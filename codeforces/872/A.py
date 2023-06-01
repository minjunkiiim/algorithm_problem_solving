t = int(input())

for _ in range(t):
    s = input()

    n = len(s)

    ret = -1
    for i in range(1, n):
        if s[i] != s[0]:
            ret = 0
            break

    if ret == -1:
        print(ret)
        continue

    l = i
    r = n - 1

    ret = n
    while l <= r:
        if s[l] != s[r]:
            ret -= 1
            break

    print(ret)