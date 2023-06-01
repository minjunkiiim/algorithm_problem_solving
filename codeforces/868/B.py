t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ret = 0
    for i in range(k):
        for j in range(i, n, k):
            if (a[j] - 1) % k != i:
                if ret < 2:
                    ret += 1
                else:
                    ret = -1
                    break
        
        if ret == -1:
            break
    
    if ret > 0:
        ret = 1
        
    print(ret)