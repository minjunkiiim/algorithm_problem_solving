t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split(' ')
    s.sort(key=lambda x:len(x))

    ret = 'YES'
    for i in range(n - 1):
        if s[2 * i] != s[2 * i + 1][::-1]:
            ret = 'NO'
            break
    print(ret)