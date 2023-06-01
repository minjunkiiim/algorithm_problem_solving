t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    ret = 'NO'
    for i in range(n):
        if arr[i] <= i + 1:
            ret = 'YES'
            break

    print(ret)