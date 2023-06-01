t = int(input())

ret = []
for _ in range(t):
    n, q = list(map(int, input().split(' ')))
    arr = input().split(' ')

    check = [False] * n
    num_check = 0

    queries = []
    for _ in range(q):
        queries.append(input().split(' '))

    for k in range(q):
        s = queries[k]
        if s[0] == '1':
            if num_check == n:
                continue
            l = int(s[1])
            r = int(s[2])

            range_ = [x for x in range(l - 1, r) if not check[x]]
            for i in range_:
                a = arr[i]
                sum_digits = 0
                for j in range(len(a)):
                    sum_digits += int(a[j])
                arr[i] = str(sum_digits)
                if len(arr[i]) == 1:
                    check[i] = True
                    num_check += 1

        else:
            x = int(s[1])
            ret.append(arr[x - 1])

print('\n'.join(ret))
