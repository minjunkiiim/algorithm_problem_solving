t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    if n % 2 == 0:
        k = 0
        for num in arr:
            k ^= num
        if k != 0:
            print(-1)
        else:
            print(0)

    else:
        k = 0
        for num in arr:
            k ^= num
        print(k)
