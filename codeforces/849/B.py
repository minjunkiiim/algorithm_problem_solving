t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    i, j = 0, 0

    ret = 'NO'
    for c in s:
        if c == 'L':
            j -= 1
        elif c == 'R':
            j += 1
        elif c == 'D':
            i -= 1
        else:
            i += 1

        if i == 1 and j == 1:
            ret = 'YES'
            break

    print(ret)

