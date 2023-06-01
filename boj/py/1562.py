N = int(input())
L = 10 ** 9

counts = {(i, tuple([1 if idx == i else 0 for idx in range(10)])): 1 for i in range(1, 10)}

for i in range(1, N):
    next_counts = {}
    for k, v in counts.items():
        j, tup = k

        if j > 0:
            next_l = list(tup)
            next_l[j - 1] = 1
            next_tup = tuple(next_l)

            next_counts[(j - 1, next_tup)] = next_counts.get((j - 1, next_tup), 0) + v

        if j < 9:
            next_l = list(tup)
            next_l[j + 1] = 1
            next_tup = tuple(next_l)

            next_counts[(j + 1, next_tup)] = next_counts.get((j + 1, next_tup), 0) + v

    counts = next_counts

complete_tup = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

r = 0
for k, v in counts.items():
    if k[1] == complete_tup:
        r = (r + v) % L

print(r)