N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

minimum = S
maximum = S
for num in arr:
    if num < 0:
        maximum -= num
    else:
        minimum -= num

counts = {0: 1}
for num in arr:
    next_counts = {}

    if num < 0:
        maximum += num
    else:
        minimum += num

    for k, v in counts.items():
        if minimum <= k and k <= maximum:
            next_counts[k] = next_counts.get(k, 0) + v
        if minimum <= k + num and k + num <= maximum:
            next_counts[k + num] = next_counts.get(k + num, 0) + v

    counts = next_counts
    
ret = counts.get(S, 0)
if S == 0:
    ret -= 1

print(ret)