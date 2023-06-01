d = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = 10 ** 9 + 7
for i in range(d + 1):
    A[i] = (A[i] - A[0]) % M
    B[i] = (B[i] - B[0]) % M


print(A)
print(B)