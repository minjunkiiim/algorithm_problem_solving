import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())

    arr = list(map(int, sys.stdin.readline().split()))

    state = 0
    ret = n

    for i in range(1, n):
        d = arr[i] - arr[i - 1]
        if d == 0:
            ret -= 1
        
        elif d < 0:
            if state < 0:
                ret -= 1
            state = -1
        else:
            if state > 0:
                ret -= 1
            state = 1

    sys.stdout.write(str(ret) + '\n')