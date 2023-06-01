t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    left = 1
    right = 1

    for i in range(n):
        right *= a[i]

    k = -1
    while left < right:
        k += 1
        left *= a[k]
        right /= a[k]


    if left != right:
        print(-1)
    else:
        print(max(1, k + 1))