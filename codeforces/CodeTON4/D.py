t = int(input())

for _ in range(t):
    q = int(input())

    L = 0
    U = -1

    retlist = []
    for q_ in range(q):
        query = list(map(int, input().split(' ')))

        if query[0] == 1:
            a, b, n = query[1:]
            l = (a - b) * (n - 1)
            u = l + a

            ret = 1

            if U == -1:
                L = l
                U = u

            else:
                if u <= L or l >= U:
                    ret = 0
                
                else:
                    L = max(L, l)
                    U = min(U, u)
            retlist.append(ret)

        else:
            if U == -1:
                retlist.append(-1)
                continue

            a, b = query[1:]

            num = (L // (a - b))
            x = (a - b) * num

            if x + a >= U:
                retlist.append(num + 1)
            else:
                retlist.append(-1)

    print(retlist)

