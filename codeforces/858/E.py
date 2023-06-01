n, q = list(map(int, input().split(' ')))

arr = [0] + list(map(int, input().split(' ')))

p = [-1, 0] + list(map(int, input().split(' ')))

dp = {i: {} for i in range(1, n + 1)}

ret = []
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split(' '))))

for x_, y_ in queries:
    x = x_
    y = y_
    if y in dp[x]:
        ret.append(dp[x][y])
        continue

    ans = 0
    while x > 0 and y > 0:
        if y in dp[x]:
            ans += dp[x][y]
            break

        ans += arr[x] * arr[y]

        x = p[x]
        y = p[y]

    ret.append(ans)

    x = x_
    y = y_
    while x > 0 and y > 0:
        if y in dp[x]:
            break
        dp[x][y] = ans
        dp[y][x] = ans
        ans -= arr[x] * arr[y]
        x = p[x]
        y = p[y]

for r in ret:
    print(r)
    