from heapq import heappush, heappop

N, K = list(map(int, input().split()))

gems = []
for _ in range(N):
    gems.append(list(map(int, input().split())))

bags = []
for _ in range(K):
    bags.append(int(input()))

gems.sort()
bags.sort()

ret = 0

q = []
i = 0
for bag in bags:
    while i < N and gems[i][0] <= bag:
        heappush(q, -gems[i][1])
        i += 1
    if q:
        ret += -heappop(q)

print(ret)

