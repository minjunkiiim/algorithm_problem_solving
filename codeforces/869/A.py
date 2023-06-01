t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    president = input()
    ret = 1

    for i in range(1, n):
        votes = input()

        if president == votes:
            ret += 1

    print(ret)
