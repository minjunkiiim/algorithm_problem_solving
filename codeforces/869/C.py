n, q = list(map(int, input().split()))

a = list(map(int, input().split()))

dels = [-1]
for i in range(1, n - 1):
    if a[i - 1] >= a[i] and a[i] >= a[i + 1]:
        dels.append(i)
dels.append(n)

rets = []
for _ in range(q):
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1

    if (r - l + 1) < 3:
        rets.append(str(r - l + 1))
        continue
    elif (r - 1 + 1) == 3:
        if a[l] >= a[l + 1] and a[r - 1] >= a[r]:
            rets.append(str(r - l))
        else:
            rets.append(str(r - l + 1))
        continue

    L = -1
    U = len(dels) - 1
    
    while L + 1 < U:
        M = (L + U + 1) // 2
        if dels[M] < l:
            L = M
        else:
            U = M
    l_idx = U

    L = 0
    U = len(dels)
    while L + 1 < U:
        M = (L + U) // 2
        if dels[M] <= r:
            L = M
        else:
            U = M
    r_idx = L

    ret = (r - l + 1) - (r_idx - l_idx + 1)
    if dels[l_idx] == l and dels[l_idx + 1] != l + 1:
        ret += 1
    if dels[r_idx] == r and dels[r_idx - 1] != r - 1:
        ret += 1
    rets.append(str(max(2, ret)))

print('\n'.join(rets))