q = int(input())

for _ in range(q):
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_ent = -1
    max_idx = -1
    for i in range(n):
        if i + a[i] <= t and b[i] > max_ent:
            max_idx = i + 1
            max_ent = b[i]

    print(max_idx)