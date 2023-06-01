t = int(input())
for _ in range(t):
    s = input()
    n = len(s)

    count_dict = {}
    for c in s:
        count_dict[c] = count_dict.get(c, 0) + 1
    count_list = sorted([[k, v] for k, v in count_dict.items()], key=lambda x:x[0])
    m = len(count_list)
    clist = [''] * n

    i = 0
    j = 0
    for i in range(m):
        c = count_list[i][0]
        count = count_list[i][1]
        count_list[i][1] = count % 2
        for _ in range(count // 2):
            clist[j] = c
            clist[n - 1 - j] = c
            j += 1

    flag = 0
    for i in range(m - 1, 0, -1):
        if count_list[i][1] == 0:
            continue            
        c = count_list[i][0]
        if flag:
            clist[n - 1 - j] = c
            j += 1
        else:
            clist[j] = c
        flag = 1 - flag

    ret = ''.join(clist)
    print(ret)

