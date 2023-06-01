N = int(input())
A = list(map(int, input().split()))
M = int(input())

X = [A[i] for i in range(N)]
X.append(0)
for i in range(N - 1, -1, -1):
    X[i] = X[i + 1] ^ X[i]


for _ in range(M):
    m, i, j, k = map(int, input().split())

    