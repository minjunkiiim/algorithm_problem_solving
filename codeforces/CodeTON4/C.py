t = int(input())

for _ in range(t):
    n, c, d = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))

    cost = 0
    max_num = -1
    
    s = set()
    for num in arr:
        if num in s:
            cost += c
        else:
            s.add(num)

        if num > max_num:
            max_num = num

    cost += (max_num - len(s)) * d
    newcost = cost
    l = sorted(list(s))

    ccost = 0
    dcost = 0
    for i in range(len(l) - 1, 0, -1):
        ccost += c
        dcost += (l[i] - l[i - 1] - 1) * d

        if ccost < dcost:
            newcost = min(newcost, cost + ccost - dcost)

    if l[0] > 1:
        ccost += c
        dcost += (l[0] - 2) * d

        if ccost < dcost:
            newcost = min(newcost, cost + ccost - dcost)

    print(newcost)