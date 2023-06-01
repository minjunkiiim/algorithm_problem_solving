t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split(' ')))
    a = abs(a)
    b = abs(b)

    ret = a + b

    if a != b:
        ret += max(a, b) - min(a, b) - 1

    print(ret)