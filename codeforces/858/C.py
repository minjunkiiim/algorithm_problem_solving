t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split(' ')))

    if n == 1:
        print(abs(p[1] - p[0]))

    elif n == 2:
        print(min(sum([abs(x) for x in p]), sum([abs(x - 2) for x in p])))

    else:
        print(sum([abs(x) for x in p]))