N = int(input())

primes = []

for n in range(2, N + 1):
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break

        i += 1

    if is_prime:
        primes.append(n)

ret = 0

l = 0
r = 0
s = 0
while r < len(primes):
    s += primes[r]

    while s > N:
        s -= primes[l]
        l += 1

    if s == N:
        ret += 1

    r += 1

print(ret)