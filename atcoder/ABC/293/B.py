n = int(input())
A = list(map(int, input().split(' ')))

check = [False] * (n + 1)

for i in range(1, n + 1):
    if not check[i]:
        check[A[i - 1]] = True

K = 0
X = []
for i in range(1, n + 1):
    if not check[i]:
        K += 1
        X.append(str(i))

print(K)
print(' '.join(X))