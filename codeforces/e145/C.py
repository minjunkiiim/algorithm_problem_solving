t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split(' ')))

    curr = 1

    ret = []
    while n > 0:
        if k >= curr:
            k -= curr
            ret.append(30)
            curr += 1

        elif k > 0:
            curr -= 1
    
            ret.append(-30 * (curr - k + 1) + 1)
            k = 0

        else:
            curr = 1
            ret.append(-999)

        n -= 1
    
    print(' '.join(list(map(str, ret))))