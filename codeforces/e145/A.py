t = int(input())

for _ in range(t):
    s = input()

    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1

    n = len(count)

    if n == 1:
        print(-1)
    
    elif n == 2:
        values = list(count.values())

        if values[0] == 2:
            print(4)

        else:
            print(6)
    
    else:
        print(4)