N, M = list(map(int, input().split()))

edges = []

for _ in range(M):
    edges.append(list(map(int, input().split())))

edges.sort(key = lambda x:-x[2])

sets = [i for i in range(N + 1)]

ret = 0
cnt = 0
while cnt < N - 2:
    v1, v2, c = edges.pop()

    path = []
    while v1 != sets[v1]:
        path.append(v1)
        v1 = sets[v1]
    for v in path:
        sets[v] = v1

    path = []
    while v2 != sets[v2]:
        path.append(v2)
        v2 = sets[v2]
    for v in path:
        sets[v] = v2    

    if v1 != v2:
        sets[v2] = v1
        cnt += 1
        ret += c

print(ret)