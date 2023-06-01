n, m = list(map(int, input().split(' ')))

adj_list = [list() for _ in range(n + 1)]
for _ in range(m):
    i, j = list(map(int, input().split(' ')))
    adj_list[i].append(j)
    adj_list[j].append(i)

for i in range(1, n + 1):
    if len(adj_list[i]) == 1:
        j = adj_list[i][0]
        adj_list[j].remove(i)
        adj_list[i] = []

print(adj_list)