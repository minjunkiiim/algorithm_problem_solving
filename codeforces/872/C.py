t = int(input())
rets = []
for _ in range(t):
    n, m = list(map(int, input().split()))

    q = list(map(int, input().split()))
    q.sort()

    num1 = 0
    num2 = 0

    ret = 0

    i = 0
    while i < n:
        if q[i] == -1:
            num1 += 1
        elif q[i] == -2:
            num2 += 1
        
        else:
            if i > 0 and q[i - 1] > 0:
                d = min(q[i] - q[i - 1], num2)
                num2 -= d
                ret += d