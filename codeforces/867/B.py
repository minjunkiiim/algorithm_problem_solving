t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 2:
        print(a[0] * a[1])
    else:
        neg = []
        pos = []
        for num in a:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)

        neg.sort()
        pos.sort(reverse=True)

        neg_max = 0
        pos_max = 0
        if len(neg) > 1:
            neg_max = neg[0] * neg[1]
        if len(pos) > 1:
            pos_max = pos[0] * pos[1]

        print(max(neg_max, pos_max))