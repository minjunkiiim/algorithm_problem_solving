import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    m = max(a) // 2
    primes = [2]
    i = 3
    while i <= m:
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            
            if i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        i += 1


    counts = {}
    for num in a:
        is_prime = True

        for p in primes:
            while num % p == 0:
                num = num // p
                counts[p] = counts.get(p, 0) + 1
                is_prime = False
            if p > num:
                break

        if is_prime:
            counts[num] = counts.get(num, 0) + 1
            
    ret = 0
    p = 0
    for k, v in counts.items():
        if v % 2 == 1:
            p += 1
            if p == 3:
                ret += 1
                p = 0
        ret += v // 2

    print(ret)