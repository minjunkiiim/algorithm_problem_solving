import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * N
s = 0
for i in range(N):
    s += arr[i]
    sum_arr[i] = s

if sum_arr[N - 1] < S:
    sys.stdout.write('0\n')
    exit()

l = 0
u = N

while l + 1 < u:
    m = (l + u + 1) // 2

    s = sum_arr[m - 1]
    if s >= S:
        u = m
        continue

    for i in range(m, N):
        s = sum_arr[i] - sum_arr[i - m]
        if s >= S:
            u = m
            break

    if u != m:
        l = m
    

sys.stdout.write(str(u) + '\n')