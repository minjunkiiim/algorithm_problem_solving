t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    actions = 0
    ptr = 0

    num_ones = 0

    for i in range(n):
        if l[i] == r[i]:
            num_ones += 1
            
        actions += l[i] - ptr + 2
        ptr = l[i]

        moves = min(k - 1, r[i] - l[i])
        
        actions += moves
        ptr += moves
        k -= moves + 1

        if k == 0:
            print(num_ones, ptr)
            while num_ones > 0 and ptr < r[i]:
                num_ones -= 1
                ptr += 1
                actions -= 2

            break

    if k > 0:
        print(-1)
    else:
        print(actions)