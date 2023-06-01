t = int(input())

for _ in range(t):
    s = input()

    ones = 0

    ret = 0
    n = len(s)
    clist = list(s)

    for i in range(n):
        c = clist[i]
        if c == '1':
            if (i >= n - 1 or clist[i + 1] == 0) and (i >= n - 2 or clist[i + 2] == 1):
                if i < n - 1:
                    c