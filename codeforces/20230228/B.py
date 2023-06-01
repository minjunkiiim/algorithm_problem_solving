t = int(input())

for _ in range(t):

    a = input()
    b = input()

    n_a = len(a)
    n_b = len(b)

    Y = False
    if a[0] == b[0]:
        print('YES')
        print(a[0] + '*')
        continue
    if a[-1] == b[-1]:
        print('YES')
        print('*' + a[-1])
        continue

    s = set()
    for i in range(n_a - 1):
        s.add(a[i : i + 2])

    for i in range(n_b - 1):
        if b[i : i + 2] in s:
            print('YES') 
            print('*' + b[i : i + 2] + '*')
            Y = True
            break

    if not Y:
        print('NO')