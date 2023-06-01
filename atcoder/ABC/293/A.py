s = input()

n = len(s)

new_s = []
for i in range(n // 2):
    c1 = s[2 * i + 1]
    c2 = s[2 * i]
    new_s.append(c1)
    new_s.append(c2)

print(''.join(new_s))