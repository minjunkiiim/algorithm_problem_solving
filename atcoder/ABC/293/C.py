def search(i, j, s, A, H, W):
    if i >= H or j >= W or A[i][j] in s:
        return 0

    if i == H - 1 and j == W - 1:
        return 1

    s.add(A[i][j])

    d = [[1, 0], [0, 1]]
    ret = 0
    for di, dj in d:
        ret += search(i + di, j + dj, s, A, H, W)

    s.remove(A[i][j])

    return ret
    

H, W = list(map(int, input().split(' ')))

A = []

for i in range(H):
    line = list(map(int, input().split(' ')))
    A.append(line)

s = set()

ret = search(0, 0, s, A, H, W)
print(ret)