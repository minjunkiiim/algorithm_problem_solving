t = int(input())

ret = []
for _ in range(t):
    s = input()

    r = 0

    prev = ''
    for c in s:
        if c == '_' and prev != '^':
            r += 1
        prev = c

    if len(s) == 1 or s[-1] == '_':
        r += 1

    ret.append(str(r))

print('\n'.join(ret))