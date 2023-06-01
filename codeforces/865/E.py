t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split(' ')))

    counts = [n + 1 for _ in range(n + 1)]

    counts[1] = 1

    dependency = [list() for _ in range(n + 1)]
    for i in range(m):
        a, b = list(map(int, input().split(' ')))

        dependency[b].append(a)

    for c in range(1, n + 1):
        for i in range(1, n + 1):
            if counts[i] == c:
                for j in dependency[i]:
                    counts[j] = min(counts[j], c + 1)

    max_c = -1
    ret = 'FINITE'
    for i in range(1, n + 1):
        c = counts[i]
        if c > n:
            ret = 'INFINITE'
            break
        
        if c > max_c:
            max_c = c

    print(ret)
    if ret == 'INFINITE':
        continue

    count_list = [list() for _ in range(max_c + 1)]

    for i in range(1, n + 1):
        count_list[counts[i]].append(i)


    ret_list = []
    for count in range(max_c, 0, -1):
        for c in range(count, max_c + 1):
                for i in count_list[c]:
                    ret_list.append(i)

    print(len(ret_list))                
    print(' '.join(list(map(str, ret_list))))


    


    
