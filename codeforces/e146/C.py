t = int(input())

for _ in range(t):
    n, s1, s2 = list(map(int, input().split(' ')))
    r = list(map(int, input().split(' ')))

    r = list(zip([i for i in range(1, n + 1)], r))

    r.sort(key=lambda x:-x[1])

    t_a = s1
    t_b = s2

    a = []
    b = []

    for idx, _ in r:
        if t_a < t_b:
            a.append(idx)
            t_a += s1
        else:
            b.append(idx)
            t_b += s2

    print(len(a), ' '.join(list(map(str, a))))
    print(len(b), ' '.join(list(map(str, b))))
     
