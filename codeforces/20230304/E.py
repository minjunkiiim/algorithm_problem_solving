from queue import Queue

n = int(input())

a = list(map(int, input().split(' ')))

a.sort()
a_dict = {}
for i in a:
    a_dict[i] = a_dict.get(i, 0) + 1
a_dict[-1] = 0

adj_list = []
for _ in range(n + 1):
    adj_list.append([])
for _ in range(n - 1):
    i, j = list(map(int, input().split(' ')))
    adj_list[i].append(j)
    adj_list[j].append(i)


candidates = {i + 1 for i in range(n)}
used = [False] * (n + 1)

for node in range(1, n + 1):
    count = 0
    q = Queue()
    dist = -1
    q.put([0, node])
    visit = [False] * (n + 1)
    visit[node] = True

    while not q.empty():
        d, v = q.get()
        if d > dist:
            if count < a_dict.get(dist, 0) or count > a_dict.get(dist, 0) + 1:
                candidates.remove(node)
                break
            if count == a_dict.get(dist, 0) + 1:
                if used[node]:
                    candidates.remove(node)
                    break
                used[node] = True
            dist = d
            count = 0

        for v2 in adj_list[v]:
            if not visit[v2]:
                q.put([d + 1, v2]) 
                visit[v2] = True
        count += 1

    if count < a_dict.get(dist, 0) or count > a_dict.get(dist, 0) + 1 and node in candidates:
        candidates.remove(node)
        break
    if count == a_dict.get(dist, 0) + 1:
        if used[node] and node in candidates:
            candidates.remove(node)
            break

print(len(candidates))
print(' '.join(map(str, sorted(list(candidates)))))
