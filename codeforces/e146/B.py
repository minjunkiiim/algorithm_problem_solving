t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split(' ')))
    
    x = a
    y = b
    if a < b:
        x = b
        y = a

    while y > 0:
        n = x % y
        x = y
        y = n

    gcd = x

    if a < b:
        tmp = a
        a = b
        b = tmp

    