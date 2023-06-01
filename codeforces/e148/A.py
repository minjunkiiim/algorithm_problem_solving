import sys

t = int(input())

for _ in range(t):
    s = sys.stdin.readline().strip()

    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1

    n = len(s)
    is_palindrome = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            is_palindrome = False
            break

    even = 0
    odd = 0
    one = 0
    for k, v in counts.items():
        if v % 2 == 0:
            even += 1
        else:
            odd += 1
        
        if v == 1:
            one += 1

    ret = 'YES\n'
    if odd > 1:
        ret = 'NO\n'
    else:
        if is_palindrome and (even == 0 or (even == 1 and (odd == 0 or one == 1))):
            ret = 'NO\n'

    sys.stdout.write(ret)