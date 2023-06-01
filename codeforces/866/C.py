t = int(input())

ret = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    nums_set = set()
    m = 0

    for num in arr:
        nums_set.add(num)
        
        while m in nums_set:
            m += 1

    if m == n:
        ret.append('No')
        continue

    nums_set = set()
    new_m = 0
    l = 0
    while l < n and arr[l] != m + 1:
        nums_set.add(arr[l])
        
        while new_m in nums_set:
            new_m += 1

        l += 1

    if l == n:
        ret.append('Yes')
        continue

    r = n - 1
    while r >= 0 and arr[r] != m + 1:
        nums_set.add(arr[r])

        while new_m in nums_set:
            new_m += 1

        r -= 1

    if new_m == m:
        ret.append('Yes')
    else:
        ret.append('No')

print('\n'.join(ret))