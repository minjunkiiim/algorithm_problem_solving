t = int(input())

for _ in range(t):
    n = int(input())
    l = 0
    r = n - 1
    p = 0
    q = n - 1
    arr = list(map(int, input().split(' ')))
    sorted_arr = sorted(arr)

    ret = '-1'
    while l < r:
        if arr[l] == sorted_arr[p]:
            l += 1
            p += 1
            continue
        if arr[l] == sorted_arr[q]:
            l += 1
            q -= 1
            continue
        if arr[r] == sorted_arr[p]:
            r -= 1
            p += 1
            continue
        if arr[r] == sorted_arr[q]:
            r -= 1
            q -= 1
            continue
        
        ret = ' '.join(map(str, [l + 1, r + 1]))
        break
    
    print(ret)
