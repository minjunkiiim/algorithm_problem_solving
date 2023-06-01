t = int(input())

for _ in range(t):
    n, d = list(map(int, input().split(' ')))
    arr = list(map(int, list(input())))
    
    for i in range(n):
        if arr[i] < d:
            arr.insert(i, d)
            break

    if len(arr) == n:
        arr.append(d)
    
    print(''.join(list(map(str, arr))))