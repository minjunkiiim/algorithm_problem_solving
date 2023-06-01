from heapq import heappush, heappop

N = int(input())

info = []
for i in range(N):
    info.append(list(map(int, input().split(' '))))
    info[i].append(i)

info.sort(key=lambda x:-x[0])

ret = []
q = []
time = 0
while info or q:
    if not q:
        t = info[-1][0]
        time = t

    else:
        _, b, i = heappop(q)
        ret.append(i + 1)
        time += b


    while info and info[-1][0] <= time:
        t, p, b, i = info.pop()
        heappush(q, [-p + t, b, i])

print(' '.join(list(map(str, ret))))