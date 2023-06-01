t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    neg = 0

    for i in range(n):
        if a[i] < 0:
            neg += 1
            a[i] = -a[i]

    a.sort()

    if neg % 2 == 1:
        a[0] = -a[0]
    print(sum(a))