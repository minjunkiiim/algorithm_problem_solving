t = int(input())
for _ in range(t):
    ret = 'YES'

    n, k = list(map(int, input().split(' ')))
    s = input()
    t = input()

    for i in range(max(n - k, 0), min(k, n)):
        if s[i] != t[i]:
            ret = 'NO'

    if sorted(s) != sorted(t):
        ret = 'NO'

    print(ret)
