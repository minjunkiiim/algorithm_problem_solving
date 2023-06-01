t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    r = -1
    
    for i in range(n):
        if p[i] == n:
            r = i
    
    ret = p[r:]

    while r > 0:
        if p[0] > p[r - 1]:
            break
        else:
            ret.append(p[r - 1])
            r -= 1

    ret += p[:r]

    print(' '.join(list(map(str, ret))))

