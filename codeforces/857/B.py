t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split(' ')))

    unknowns = 0
    knowns = 0

    max_s = 0
    for i in b:
        if i == 1:
            unknowns += 1

        else:
            knowns += unknowns
            unknowns = 0

        s = unknowns
        if knowns > 0:
            s += (knowns // 2 + 1)
        if s > max_s:
            max_s = s

    print(max_s)