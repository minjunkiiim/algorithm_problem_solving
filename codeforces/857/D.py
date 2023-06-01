t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = list(map(int, input().split(' ')))
        ai_sorted = [[a[i], i] for i in range(n)]
        a_sorted = sorted(a)
        bi_sorted = [[b[i], i] for i in range(n)]
        b_sorted = sorted(b)    

    print(a_sorted)
    print(b_sorted)