t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    max_count = 0
    count = 0

    for num in arr:
        if num == 0:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0


    print(max_count)