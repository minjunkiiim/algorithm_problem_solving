t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ret = 'YES'
    mode = 0
    for i in range(n // 2):
        l = s[i]
        r = s[n - 1 - i]

        if l != r:
            if mode == 0:
                mode += 1
            elif mode > 1:
                ret = 'NO'
                break
        else:
            if mode == 1:
                mode += 1
    
    print(ret)