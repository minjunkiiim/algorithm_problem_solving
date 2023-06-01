t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    ret = 'YES'
    for i in range(n):
        if (a[i] <= a[n - 1] and b[i] <= b[n - 1]) or (a[i] <= b[n - 1] and b[i] <= a[n- 1]):
            continue
        
        ret = 'NO'
    
    print(ret)