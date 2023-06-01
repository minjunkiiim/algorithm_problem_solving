import sys
from heapq import heappop, heappush


n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
k = list(map(int, sys.stdin.readline().split()))

for i in range(q):
    red = [True] * n

    queue = []
    for j in range(n):
        heappush(q, [a[j], j])

    l = 1
    r = k[i]

    ops = 0

    while ops < k[i]:
        num, idx = heappop(q)

        if red[idx]:
            num += r
            r -= 1
            heappush([num, idx])
        
        else:
            if ops == k[i] - 1
        ops += 1

    