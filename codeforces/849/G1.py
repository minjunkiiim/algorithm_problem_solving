t = int(input())

for _ in range(t):
    n, c = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))

    for i in range(n):
        arr[i] += i + 1

    arr.sort()

    i = 0
    while i < n:
        c -= arr[i]
        if c < 0:
            break
        i += 1
    
    print(i)
        

