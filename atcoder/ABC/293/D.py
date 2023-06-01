N, M = list(map(int, input().split(' ')))

groups = {i: {i} for i in range(1, N + 1)}
cycles = 0
num_groups = N
for m in range(M):
    a, b, c, d = input().split(' ')
    a = int(a)
    c = int(c)

    if a in groups[c]:
        cycles += 1
    else:
        group = groups[a] | groups[c]

        for i in group:
            groups[i] = group

        num_groups -= 1
print(cycles, num_groups - cycles)