t = int(input())

cf = "codeforces"
for _ in range(t):
    s = input()
    ret = 0
    for i in range(10):
        if s[i] != cf[i]:
            ret += 1

    print(ret)