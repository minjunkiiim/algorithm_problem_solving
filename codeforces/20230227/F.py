t = int(input())
for _ in range(t):
    n, b, k1, k2 = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))

    a.sort(key=lambda x:-x)

    for i in range(k1):
        a[i] = (a[i] + 1) // 2

    a.sort(key=lambda x:-x)
    print(a)
    for i in range(k2):
        a[i] = max(a[i] - b, 0)
    print(a)
    print(sum(a))