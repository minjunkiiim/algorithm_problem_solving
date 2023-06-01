t = int(input())

ret = []
for _ in range(t):
    s = input()

    r = 1
    if s[0] == '0':
        r = 0
        
    elif s[0] == '?':
        r = 9

    for i in range(1, len(s)):
        if s[i] == '?':
            r *= 10

    ret.append(str(r))    

print('\n'.join(ret))    
