t = int(input())

for _ in range(t):
    arr = list(input())
    n = len(arr)
    ret = [[], []]

    f = 0
    for i in range(n):
        a = int(arr[i])
        if a % 2 == 0:
            x = a // 2
            ret[0].append(str(x))
            ret[1].append(str(x))
        else:
            x = a // 2
            y = x + 1

            ret[f].append(str(x))
            ret[1 - f].append(str(y))

            f = 1 - f

    print(str(int(''.join(ret[0]))), str(int(''.join(ret[1]))))
