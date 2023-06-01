t = int(input())

ret = []
for _ in range(t):
    s = input()
    n = len(s)

    max_ones = 0
    ones = 0
    for _ in range(2):
        for c in s:
            if c == '0':
                ones = 0
            else:
                ones += 1
                if ones > max_ones:
                    max_ones = ones 

    r = 0
    if max_ones > n:
        r = n * n
    else:
        r = ((max_ones + 1) // 2) * ((max_ones + 2) // 2)
    ret.append(str(r))

print('\n'.join(ret))