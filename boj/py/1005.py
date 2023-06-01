from collections import deque

T = int(input())

ret = []

for _ in range(T):

    N, K = list(map(int, input().split(' ')))

    D = [0] + list(map(int, input().split(' ')))

    in_edges = [set() for _ in  range(N + 1)]
    out_edges = [set() for _ in range(N + 1)]
    for k in range(K):
        X, Y = list(map(int, input().split(' ')))

        out_edges[X].add(Y)
        in_edges[Y].add(X)

    W = int(input())

    q = deque()
    for i in range(1, N + 1):
        if len(in_edges[i]) == 0:
            q.appendleft(i)

    sorted_list = []        
    while q:
        v = q.pop()
        sorted_list.append(v)

        for u in out_edges[v]:
            in_edges[u].remove(v)

            if len(in_edges[u]) == 0:
                q.appendleft(u)

    built_time = D[:]

    for v in sorted_list:
        for u in out_edges[v]:
            built_time[u] = max(built_time[u], built_time[v] + D[u])

    ret.append(str(built_time[W]))


print('\n'.join(ret))