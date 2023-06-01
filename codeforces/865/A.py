t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split(' ')))

    if a == 1 or b == 1:
        print(1)
        print(a, b)

    else:
        print(2)
        print(1, b - 1)
        print(a, b)