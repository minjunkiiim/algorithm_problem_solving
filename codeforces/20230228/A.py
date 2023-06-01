t = int(input())
S = 'FBFFBFFBFBFFBFFBFBFFBFFB'

for _ in range(t):
    k = int(input())
    s = input()

    if s in S:
        print('YES')
    else:
        print('NO')
