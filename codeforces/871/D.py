t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    num = 0
    p = n
    while p % 3 == 0:
        p = p // 3
        num += 1
    
    if m % p != 0:
        print('NO')
        continue
    m = m // p

    num2 = 0
    num3 = 0

    while m % 2 == 0:
        m = m // 2
        num2 += 1
    while m % 3 == 0:
        m = m // 3
        num3 += 1

    if m != 1 or num2 + num3 > num:
        print('NO')
    else:
        print('YES')