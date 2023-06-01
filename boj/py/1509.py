S = input()

n = len(S)

jumps = [list() for _ in range(n)]

for i in range(n):
    k = 0
    while i - k >= 0 and i + k < n:
        if S[i - k] != S[i + k]:
            break

        jumps[i - k].append(i + k + 1)
        k += 1
        
    k = 0
    while i - k >= 0 and i + k + 1 < n:
        if S[i - k] != S[i + k + 1]:
            break
        
        jumps[i - k].append(i + k + 2)
        k += 1

dist = [n + 1] * (n + 1)
dist[0] = 0

d = 1
while d <= n:
    for i in range(n):
        if dist[i] == d - 1:
            for j in jumps[i]:
                dist[j] = min(dist[j], d)

    d += 1

    if dist[n] < n + 1:
        break

print(dist[n])
