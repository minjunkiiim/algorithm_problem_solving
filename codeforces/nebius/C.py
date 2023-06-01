t = int(input())

for _ in range(t):
    n, x, p = list(map(int, input().split(' ')))

    target = (n - x) % n

    ret = 'NO'
    curr = 0
    for i in range(1, min(2 * n, p + 1)):
        curr = (curr + i) % n
        
        if curr == target:
            ret = 'YES'
            break

    print(ret)