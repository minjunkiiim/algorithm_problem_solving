t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    likes = 0
    removes = 0

    for k in a:
        if k > 0:
            likes += 1
        else:
            removes += 1

    max_arr = [i + 1 for i in range(n)]
    min_arr = [1 if i % 2 == 0 else 0 for i in range(n)]

    for i in range(likes, n):
        max_arr[i] = max_arr[i - 1] - 1

    for i in range(max(removes * 2, 1), n):
        min_arr[i] = min_arr[i - 1] + 1

    print(' '.join(list(map(str, max_arr))))
    print(' '.join(list(map(str, min_arr))))
