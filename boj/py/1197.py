from heapq import heappush, heappop, heapify

V, E = list(map(int, input().split()))

adj_list = [list() for _ in range(V + 1)]

for _ in range(E):
    A, B, C = list(map(int, input().split()))
    adj_list[A].append([C, B])
    adj_list[B].append([C, A])

span = {1}
q = [[w, v] for w, v in adj_list[1]]
heapify(q)

sum_w = 0
while len(span) < V:
    w, v = heappop(q)
    if v in span:
        continue

    span.add(v)

    sum_w += w

    for nw, nv in adj_list[v]:
        if nv not in span:
            heappush(q, [nw, nv])

print(sum_w)