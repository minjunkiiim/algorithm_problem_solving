t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    chars = [[], ['m', 'M'], ['e', 'E'], ['o', 'O'], ['w', 'W']]
    state = 0
    ret = 'YES'
    for i in range(n):
        c = s[i]
        if c in chars[state]:
            continue
        else:
            state += 1
            if state >= 5 or c not in chars[state]:
                ret = 'NO'
                break
    if state <= 3:
        ret = 'NO'
    print(ret)
            