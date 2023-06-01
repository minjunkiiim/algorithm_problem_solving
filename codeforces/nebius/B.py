t = int(input())

for _ in range(t):
    n, k, d, w = list(map(int, input().split(' ')))
    T = list(map(int, input().split(' ')))

    ret = 0
    curr_pack = 0
    open_time = 0

    for t in T:
        if not curr_pack:
            curr_pack = k - 1
            ret += 1
            open_time = t + w

        else:
            if open_time + d >= t:
                curr_pack -= 1
            else:
                curr_pack = k - 1
                ret += 1
                open_time = t + w

    print(ret)