t = int(input())
for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split(' ')))

    i = 0
    j = 0
    cost = []
    score = 1
    for j in range(n):
        score = score * (seq[j]) / (j - i + 1)
        r = seq[i] / (j - i + 1)
        while r < 1 and i < j:
            i += 1
            r = seq[i] / (j - i + 1)
        cost.append(j - i + 1)
    
    print(' '.join(list(map(str, cost))))
