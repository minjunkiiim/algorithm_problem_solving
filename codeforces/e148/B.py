import sys

t = int(input())

for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))

    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    l = 0
    r = n - k

    s = sum(arr[:r])
    ret = s

    for i in range(k):
        s += arr[r] - arr[l] - arr[l + 1]
        l += 2
        r += 1

        ret = max(ret, s)

    sys.stdout.write(str(ret) + '\n')
