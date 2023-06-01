t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    grid = []

    for i in range(n):
        grid.append(list(map(int, input().split())))

    d = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    max_vol = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue

            vol = 0
            stack = [[i, j]]
            while stack:
                x, y = stack.pop()
                
                if grid[x][y] == 0:
                    continue

                vol += grid[x][y]
                grid[x][y] = 0

                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == 0:
                        continue
                    stack.append([nx, ny])
                
            max_vol = max(vol, max_vol)
    
    print(max_vol)
