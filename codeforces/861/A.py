t = int(input())

for _ in range(t):
    l, r = list(map(int, input().split(' ')))

    d = -1
    ret = -1

    for k in range(l, r + 1):
        num = k
        dlist = []
        while num:
            dlist.append(num % 10)
            num = num // 10

        M = max(dlist)
        m = min(dlist)

        if M - m > d:
            ret = k
            d = M - m

            if d == 9:
                break

    print(ret)