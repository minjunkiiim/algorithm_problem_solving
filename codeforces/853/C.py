t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split(' ')))

    log = [list() for _ in range(m + n + 1)]
    
    arr = list(map(int, input().split(' ')))
    
    for a in arr:
        log[a].append(0)

    for i in range(1, m + 1):
        p, v = list(map(int, input().split(' ')))
        p -= 1
        log[arr[p]].append(i)
        log[v].append(i)
        arr[p] = v

    for a in arr:
        log[a].append(m + 1)

    ret = 0
    for i in range(1, m + n + 1):
        count = 0
        l = log[i]

        for j in range(len(l) // 2):
            count += l[j * 2 + 1] - l[j * 2]

        ret += count * (m + 1 - count) + count * (count - 1) // 2


    print(ret)