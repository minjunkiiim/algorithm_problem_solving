from heapq import heappush, heappop

N, M = list(map(int, input().split()))

in_req = [list() for _ in range(N)]
out_req = [list() for _ in range(N)]

for _ in range(M):
    A, B = list(map(int, input().split()))

    in_req[B].append(A)
    out_req[A].append(B)

ret = []

q = []
for i in range(N):
    if len(in_req[i]) == 0:
        heappush(q, i)

        for j in out_req[i]:
            in_req[j].remove(i)

        

    