t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    ret = 'NO'
    if n % 2 == 1:
        ret = 'YES'

    else:
        for i in range(1, n - 1):
            diff = a[0] - a[i]
            a[i] += diff
            a[i + 1] += diff

        if a[n - 1] >= a[0]:
            ret = 'YES'

    print(ret)
