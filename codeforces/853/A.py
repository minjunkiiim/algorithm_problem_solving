t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    ret = 'NO'

    for i in range(n):
        for j in range(i + 1, n):
            x = max(a[i], a[j])
            y = min(a[i], a[j])
            while y > 0:
                temp = y
                y = x % y
                x = temp
            if x <= 2:
                ret = 'YES'
                break

        if ret == 'YES':
            break


    print(ret)
