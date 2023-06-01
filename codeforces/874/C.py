t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = set()
    odd = set()

    for num in a:
        if num % 2 == 0:
            even.add(num)
        else:
            odd.add(num)

    ret = 'YES'
    if len(odd) > 0 and len(even) > 0:
        min_odd = min(odd)
        for num in a:
            if num % 2 == 0 and num < min_odd:
                ret = 'NO'
                break
            
    print(ret)