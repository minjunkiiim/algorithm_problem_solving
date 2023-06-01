t = int(input())

s = set(list('codeforces'))

for _ in range(t):
    c = input()
    if c in s:
        print('YES')
    else:
        print('NO')