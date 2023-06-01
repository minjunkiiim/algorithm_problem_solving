t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    counts = [0] * (n + 1)
    
    for i in range(m):
        u, v = list(map(int, input().split()))
        counts[u] += 1
        counts[v] += 1

    ones = 0
    nums = {}
    for i in range(1, n + 1):
        if counts[i] == 1:
            ones += 1
        else:
            nums[counts[i]] = nums.get(counts[i], 0) + 1

    x = 0
    y = 0
    if len(nums) == 1:
        x = list(nums.keys())[0]
        y = x - 1

    else:
        for k, v in nums.items():
            if v == 1:
                x = k
            else:
                y = k - 1

    print(x, y)

    