t = int(input())

M = 200001

for _ in range(t):
    n = int(input())

    min_s1 = M
    min_s2 = M
    min_both = 2 * M

    for i in range(n):
        m, s = input().split()

        if s == '10':
            min_s1 = min(min_s1, int(m))
        elif s == '01':
            min_s2 = min(min_s2, int(m))
        elif s == '11':
            min_both = min(min_both, int(m))

    if min_both == 2 * M and (min_s1 == M or min_s2 == M):
        print(-1)
    else:
        print(min(min_s1 + min_s2, min_both))