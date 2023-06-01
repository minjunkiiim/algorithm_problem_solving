t = int(input())

for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    l = n
    r = -1

    for i in range(n):
        if a1[i] != a2[i]:
            l = min(l, i)
            r = max(r, i)

    while l > 0 and a2[l - 1] <= a2[l]:
        l -= 1
    
    while r < n - 1 and a2[r] <= a2[r + 1]:
        r += 1

    print(l + 1, r + 1)