def f(n):
    if n == 1:
        return []

    if n % 2 == 0:
        return None

    ret = f((n - 1) // 2)
    if ret is not None:
        ret.append(2)
        return ret
    
    ret = f((n + 1) // 2)
    if ret is not None:
        ret.append(1)
        return ret

    return None


t = int(input())

for _ in range(t):
    n = int(input())

    ret = f(n)
    if ret is None:
        print(-1)
        
    else:
        print(len(ret))
        print(' '.join(list(map(str, ret))))
