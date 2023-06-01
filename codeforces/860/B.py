t = int(input())

for _ in range(t):
    m = int(input())

    candidates = [set() for _ in range(m)]

    for i in range(m):
        n = int(input())
        a = list(map(int, input().split(' ')))
        candidates[i] = set(a)

        for num in a:
            for j in range(i):
                if num in candidates[j]:
                    candidates[j].remove(num)

    ret = []
    for candidate in candidates:
        if len(candidate) < 1:
            ret = -1
            break
        ret.append(str(list(candidate)[0]))

    if ret == -1:
        print(ret)
    else:
        print(' '.join(ret))
    